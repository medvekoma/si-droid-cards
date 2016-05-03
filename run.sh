#!/usr/bin/env bash
tstamp=$(date +"%Y-%m-%d")
tempfile=tmp$tstamp.csv
utf8file=si-$tstamp.csv
python retrievecards.py > $tempfile
iconv -f L1 -t UTF8 $tempfile | sed 's/õ/ő/g' | sed 's/Õ/Ő/g' | sed 's/û/ű/g' > $utf8file 
