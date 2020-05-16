def encrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in key:
        for i in range(len(msg)):
            if i == 0:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[-1])
            else:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[i-1])

            while tmp > 255:
                tmp -= 256
            msg[i] = chr(tmp)
    return ''.join(msg)

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

cipher = b'''?ף??,L?
>?2Xբ
|??I?)?E?-?˒\/;?ǲy?[w#M??2?~??Y@'?缘??泣,????P??@5??f$?\*r?wF??3?g?X?}?i6??~?K??Y?Ŏ???'%??e?>?x?o?+g?/?K?>?^??V??N?k??e'''

print decrypt("71115","5b983aea3fc834acc10d8233686a76fd")
