#!/bin/bash

while read line
do
  eval 'http POST http://wlxyzlw.iptime.org:8008/address/ address="$line"' < /dev/tty
done < address.txt
