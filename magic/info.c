#include <unistd.h>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

using namespace std;

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

int main() {
    setuid(0);
    setgid(0);
    cout << "====================Hardware Info====================" << endl;
    cout << exec("lshw -short") << endl;
    cout << "====================Disk Info====================" << endl;
    cout << exec("fdisk -l") << endl;
    cout << "====================CPU Info====================" << endl;
    cout << exec("cat /proc/cpuinfo") << endl;
    cout << "====================MEM Usage=====================" << endl;
    cout << exec("free -h");
    return(0);
}
