#!/usr/bin/python3
def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)

cipher = '''?ף??,L?
>?2Xբ
|??I?)?E?-?˒\/;?ǲy?[w#M??2?~??Y@'?缘??泣,????P??@5??f$?\*r?wF??3?g?X?}?i6??~?K??Y?Ŏ???'%??e?>?x?o?+g?/?K?>?^??V??N?k??e'''

cipher = list(cipher)
for index in range(len(cipher)):
    if ord(cipher[index]) > 256:
        cipher[index] = chr(ord(cipher[index])%256)

print(''.join(cipher))
# with open("../../wordlists/rockyou.txt") as rockyou:
#     print("trying")
#     for line in rockyou:
#         line = line.rstrip('\n')
#         key = line
#         if "recovery" in decrypt(key, cipher):
#             print(key)
#             print(decrypt(key, cipher))
#             break
#         else:
#             print(key)
