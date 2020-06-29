#!/bin/bash
while true; do
FILE="/var/www/jobs/$(date +'%Y-%m-%d_%T')"
if [[ -f $FILE ]]; then
    ln -sf /home/sam $FILE
    echo "Found $FILE"
    break
fi
done
