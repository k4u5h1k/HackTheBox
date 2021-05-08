#!/usr/bin/python3
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
"Cookie" : f"auth={sys.argv[1]}",
"Upgrade-Insecure-Requests": "1",
"Cache-Control": "max-age=0"
}
# print(sys.argv[1])
print( requests.get("http://intense.htb/submit",headers=headers) )
