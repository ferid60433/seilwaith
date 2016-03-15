#!/bin/bash

prompts2wlist samples.txt wlist

echo "SENT_START" >> wlist
echo "SENT_END" >> wlist

cp /usr/local/srdk/htk/sort.py .
python sort.py wlist
rm sort.py

