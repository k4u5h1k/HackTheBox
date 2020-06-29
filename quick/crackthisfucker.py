#!/usr/bin/python3
import hashlib
import crypt
with open("../../wordlists/rockyou.txt",errors="ignore") as handle:
    for line in handle:
        word = line.rstrip()
        if hashlib.md5(crypt.crypt(word,'fa').encode()).hexdigest() == 'e626d51f8fbfd1124fdea88396c35d05':
            print("password is : ",word)
            break
        else:
            print("tried : ",word)


