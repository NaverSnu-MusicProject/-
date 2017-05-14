#!/bin/bash
a=0
while read line
do
  case $a in
    9) sleep 1;;
    *) echo "reading";;
  esac
  echo $line
  a=`expr $a + 1`
  a=`expr $a % 10`
done < test.txt
