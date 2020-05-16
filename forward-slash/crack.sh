#!/bin/bash
ln -s /var/backups/config.php.bak $(echo -n $(date +"%T") | md5sum| awk '{print $1}')
echo $(date +"%T")
echo $(echo -n $(date +"%T") | md5sum| awk '{print $1}')
backup


