#!/usr/bin/python3
from binascii import unhexlify
from base64 import b64encode

myhash = input("enter hash : ")
print(b64encode(unhexlify(myhash)))

