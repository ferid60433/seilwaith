#!/bin/bash

rm -rf /srdk_projects/cy/braichrobot
mkdir -p /srdk_projects/cy/braichrobot/audio

cd /srdk_projects/cy/braichrobot
wget -r --no-parent http://techiaith.cymru/corpws/BraichRobot/

mv -v techiaith.cymru/corpws/BraichRobot/* .

cd audio
mkdir wav
mkdir mfcc

mv -v *.zip wav

cd wav
unzip \*.zip
rm *.zip 

cd ../..
rm -rf techiaith.cymru

