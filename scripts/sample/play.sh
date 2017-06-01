#!/bin/bash
a=0
while read line
do
  case $a in
    0) date=$line;;
    1) track=$line;;
    2) address=$line
    echo $date
    echo $track
    echo $address
    eval 'http POST http://wlxyzlw.iptime.org:8008/play/ date="$date" track="$track" address="$address"' < /dev/tty;;
  esac
  a=`expr $a + 1`
  a=`expr $a % 3`
done < play.txt
