#!/usr/bin/python3
from os import listdir,path
logdir = input()
if logdir:
    if not path.exists(f"app/{logdir}"):
        print(f"Can't find {logdir}")
    else:
        print(listdir(logdir))
# return str(logdir)

