#!/bin/bash

echo
echo '-----------------------------------------------------------------------------------------------'
echo 'Welcome to the loan aggregator application.'
echo 'Please enter the full path to your input file or its name if it exists in the current directory.'
echo 'For example /user/home/Loans.csv or Loans.csv'
read filename
echo

#check if file exists
echo "Checking if file exists..."
if [ -f $filename ];then
    echo "File $filename found."
else
    echo "File $filename does not exist!"
    echo "Program exiting..."
    exit 1
fi
echo

#check if file is empty
echo "Checking if file is empty..."
if [ -s $filename ]
then
    echo "File $filename does contain some contents."
else
    echo "File $filename is empty!"
    echo "Program exiting..."
    exit 1
fi
echo

#create output file and fill it with output header
echo "Network,Product,Month,Amount,Counter" > Output.csv

#Processing the data
echo 'Processing ...'

cat $filename \
| awk -f accept_only_five_columns.sh \
| python3 mapper.py \
| ./sort_loans.sh \
| python3 reducer.py \
>> Output.csv

echo "In the file $filename, only entries with exactly five lines will be processed."
echo "All errors in the data have been logged in the file app.log which will be in the current directory"

echo
echo "The final results are contained in the file Output.csv in the current directory"
echo "Program ending..."
echo

