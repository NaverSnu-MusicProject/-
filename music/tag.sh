#!/bin/bash
a=0
while read line
do
  case $a in
    0) name=$line;;
    1) score=$line
    eval 'http POST http://wlxyzlw.iptime.org:8008/tag/ tag_name=$name tag_score=$score' < /dev/tty;;
  esac
  a=`expr $a + 1`
  a=`expr $a % 2`
done < tag.txt
