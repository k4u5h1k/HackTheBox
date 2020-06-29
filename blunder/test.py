#!/usr/bin/python3
with open("../../wordlists/rockyou.txt") as handle:
        for line in handle:
            try:
                print(line.rstrip())
            except:
                continue

    


