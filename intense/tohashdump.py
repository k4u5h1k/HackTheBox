from binascii import hexlify,unhexlify
from hashlib import sha256
from base64 import b64decode

b64 = input("enter second part :")
decoded = b64decode(b64)
hash = hexlify(decoded)
print(hash)
