#!/bin/bash
a=0
while read line
do
  case $a in
    0) id=$line;;
    1) date=$line;;
    2) track=$line;;
    3) tag=$line;;
    4) harmony=$line
    eval 'http POST http://wlxyzlw.iptime.org:8008/mtm/ mtm_id=$id mtm_date="$date" track=$track tag=$tag harmony=$harmony' < /dev/tty;;
  esac
  a=`expr $a + 1`
  a=`expr $a % 5`
done < mtm.txt
