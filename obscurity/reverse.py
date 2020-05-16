#!/usr/bin/python3
def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted

def encrypt(text, key):
    keylen = len(key)
    keyPos = 0
    encrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr + ord(keyChr)) % 255)
        encrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return encrypted

encrypted_text = "¦ÚÈêÚÞØÛÝÝ×ÐÊßÞÊÚÉæßÝËÚÛÚêÙÉëéÑÒÝÍÐêÆáÙÞãÒÑÐáÙ¦ÕæØãÊÎÍßÚêÆÝáäèÎ"
decrypted_text = "Encrypting this file with your key should result in out.txt, make sure your key is correct!"
# for x in encrypted_text:
#         keyChr = key[keyPos]
#         newChr = ord(x)
#         newChr = chr((newChr + ord(keyChr)) % 255)
#         encrypted += newChr
#         keyPos += 1
#         keyPos = keyPos % keylen
key=""
for x,y in zip(encrypted_text,decrypted_text):
    key+=chr(ord(x)-ord(y))

print(decrypt('´ÑÈÌÉàÙÁÑé¯·¿k', key))
