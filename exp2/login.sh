#!/bin/bash
echo "Enter username:"
read a
who > userlist
if grep $a userlist
then
echo "user logged in"
else
echo "user not logged in"
fi