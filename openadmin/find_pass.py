from hashlib import sha512
with open("/Users/Kaushik/stuff/ctf/openadmin/ninjas.txt","r") as f:
    for line in f:
        if sha512(str.encode(line)).hexdigest() == "00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758eebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1":
            print(line)