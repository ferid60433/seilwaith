#!/bin/bash

# create lexicon
cat cymraegmdb_lexicon prompts > source_lexicon 
cat source_lexicon | python 3col_lexicon.py > lexicon

echo "MAE'N_HWYR                  [MAE'N_HWYR]                m AE n h w Y r" >> lexicon

echo "SENT_END        []      sil" >> lexicon
echo "SENT_START      []      sil" >> lexicon

cp /usr/local/srdk/htk/sort.py .
python3 sort.py lexicon
rm sort.py
rm source_lexicon

