#!/usr/bin/python3
import requests
import re
url="http://10.10.10.168:8080/"
with open("/Users/Kaushik/stuff/wordlists/directory-list-2.3-medium.txt") as f:
    for line in f:
        if not re.search("404",requests.get(f"{url}{line}").text):
            print(line)
