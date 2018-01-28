#!/bin/sh

files="./imgdataset/*"
for filepath in $files; do
    echo $filepath
    SECONDS=0
    python main.py $filepath > Filename_Analogy
    fname="${filepath%.*}"
    fname="${fname#*/*/}"
    sort Filename_Analogy > ./res/$fname
    time=$SECONDS
    echo $time
done
#cat Filename_Analogy_sorted | cut -d' www' -f2 > Analogy_sorted
