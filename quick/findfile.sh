#!/bin/bash
FILE="/var/www/jobs/$(date +'%Y-%m-%d_%T')"
while true; do
if [[ -f $FILE ]]; then
    echo "Found $FILE"
    cat $FILE
    echo "done catting"
    ./$FILE
fi
done
