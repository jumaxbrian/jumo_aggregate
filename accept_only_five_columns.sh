#!/bin/bash
# set the field separator as a comment
BEGIN{FS = ","}

#print only lines with five columns and exclude first line which contains column headers
NF == 5 && NR > 1 { print }