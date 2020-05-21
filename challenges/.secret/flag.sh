#!/bin/bash
for i in {1..35}
do
    find . -exec ls {} \; | grep '/$i$' | awk '{split($0,a,"/"); print a[2]}' ORS="" >> flag
done


