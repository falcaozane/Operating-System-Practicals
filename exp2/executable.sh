#!/bin/bash
echo "Enter a filename: " 
read filename 
if [ -x "$filename" ]; then 
echo "$filename is already executable." 
else 
chmod +x "$filename"
 echo "$filename is now executable." 
fi 