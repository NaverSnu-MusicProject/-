#!/bin/bash
a=0
while read line
do
  case $a in
    0) id=$line;;
    1) title=$line;;
    2) is=$line
    eval 'http POST http://wlxyzlw.iptime.org:8008/track/ track_id=$id track_title="$title" is_title=$is' < /dev/tty;;
  esac
  a=`expr $a + 1`
  a=`expr $a % 3`
done < track.txt
