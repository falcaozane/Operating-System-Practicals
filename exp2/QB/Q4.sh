#!/bin/bash

echo "Enter Size(N)"
read N
echo "Enter Numbers"
for((i=1;i<=N;i++))
do
    read num
    sum=$((num+sum))
done
echo $sum
