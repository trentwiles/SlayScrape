#!/bin/bash

file="domain2multi-dev.txt"

while read x
do
python3 main-no-wipe.py $x
done < $file
