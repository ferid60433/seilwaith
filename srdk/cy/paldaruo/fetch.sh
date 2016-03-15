#!/bin/bash

rm -rf /srdk_projects/cy/corpus/audio/paldaruo
mkdir -p /srdk_projects/cy/corpus/audio/paldaruo

cd /srdk_projects/cy/corpus/audio/paldaruo
wget -r --no-parent http://techiaith.cymru/corpws/Paldaruo/

mv -v techiaith.cymru/corpws/Paldaruo/* .

find . -name "index.*" -type f -delete

mv audio/wav .
rm audio
cd wav
unzip \*.zip
rm *.zip 
cd -

rm -rf techiaith.cymru

python /usr/local/srdk/cy/paldaruo/correct_wav_extensions.py

