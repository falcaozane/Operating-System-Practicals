#!/bin/bash
echo "Enter a number to countdown from"
read count
until [ $count -le 0 ]
do
echo count: $count
((count=count-1))
done
echo "Happy New Year!!"