#!/bin/bash

echo "Enter the number(N)"
read N
if [[ "$N" != [0-9] ]];then
    echo "not in range"
else
    echo "number within range"
fi