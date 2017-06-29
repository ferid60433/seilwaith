#!/bin/bash

rm -rf /srdk_projects/cy/corpus/audio/paldaruo
mkdir -p /srdk_projects/cy/corpus/audio/paldaruo

cd /srdk_projects/cy/corpus/audio/paldaruo
git -c http.sslVerify=false clone --branch v3.0 --depth 1 https://git.techiaith.bangor.ac.uk/Data-Porth-Technolegau-Iaith/Corpws-Paldaruo.git
mv -v Corpws-Paldaruo/* .

rm -rf Corpws-Paldaruo

mv audio/wav .
rmdir audio

cd wav
unzip \*.zip
rm *.zip 
cd -

# downsample to 16kHz
source /usr/local/srdk/htk/downsample.sh paldaruo
