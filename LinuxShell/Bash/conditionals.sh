#!/bin/bash
read char

if [[ $char == ['Yy'] ]]            # if the character entered by the user is 'y' or 'Y'.. then it should display 'YES'
then
  echo "YES"
elif [[ $char == ['Nn'] ]]          # if the character entered by the user is 'n' or 'N'.. then it should display 'NO'
then
   echo "NO"  
   
fi   
