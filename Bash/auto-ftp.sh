#!/bin/bash

HOST='172.18.70.88 21'
USER='bnbsking'
PASSWD="$1"

cd ./test/crontabTrash
for filename in *; do
	ftp -n $HOST <<END_SCRIPT
	quote USER $USER
	quote PASS $PASSWD
	put "$filename"
	quit
END_SCRIPT
rm "$filename"
done

