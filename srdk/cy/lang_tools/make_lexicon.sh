#!/bin/bash

# create lexicon
cat cymraegmdb_lexicon | python llef/htk_annotate.py > lexicon

echo "SENT_END        []      sil" >> lexicon
echo "SENT_START      []      sil" >> lexicon

