#!/bin/bash
path=$1 
echo $path
while ( true ) ; do 
	file=$(ls $path) 
	if [ "${file}" == "" ] 
	then 
		echo $file
		continue
	else 
		mv $path/$file ./
		break
       	fi 
done
