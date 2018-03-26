#!/bin/bash

files="$1/*"

for f in $files; do
    echo $f
    fname="${f#*/*/}"
    cut -d ',' -f 2 $f > ./kmeansres/$fname
done
