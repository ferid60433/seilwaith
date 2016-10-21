cat cymraegmdb_lexicon phrases > source_lexicon  
cat source_lexicon | python 2col_lexicon.py > lexicon
echo "MAE'N_HWYR m AE1 n h w Y r" >> lexicon

cp /usr/local/srdk/htk/sort.py .
python3 sort.py lexicon
rm sort.py
rm source_lexicon
