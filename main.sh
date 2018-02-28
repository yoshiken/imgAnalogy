#!/bin/sh

files="./imgdataset/*"

if [ ! -e $2 ] ; then
        mkdir $2
fi

for f in $files; do
    echo $f
    SECONDS=0
    python $1 $f > Filename_Analogy
    fname="${f%.*}"
    fname="${fname#*/*/}"
    sort Filename_Analogy > ./$2/$fname
    time=$SECONDS
    echo $time
done
