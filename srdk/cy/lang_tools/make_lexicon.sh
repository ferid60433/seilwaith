#!/bin/bash

# create lexicon
cat cymraegmdb_lexicon | python 3col_lexicon.py > lexicon

echo "SENT_END        []      sil" >> lexicon
echo "SENT_START      []      sil" >> lexicon

