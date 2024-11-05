#!/bin/bash

HOST='10.32.1.251'
USER='bnbsking'
PASSWD="$1"

cd ./test/crontabTrash
for filename in *; do
	echo "$filename"
	lftp sftp://$USER:$1@$HOST << END_SFTP
	cd ./Desktop/FTPshared
	put "$filename"
	quit	
END_SFTP
rm "$filename"
done
