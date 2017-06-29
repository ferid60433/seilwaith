#!/bin/bash
CORPUS_NAME="$1"
AUDIO_DIRS=($(find /srdk_projects/cy/corpus/audio/${CORPUS_NAME}/wav -maxdepth 1 -type d))

echo ${#AUDIO_DIRS[@]}

for a in "${AUDIO_DIRS[@]}" 
do
	echo "Found : $a"
	mkdir -p $a/48kHz

	WAV_FILES=($(find $a -maxdepth 1 -type f -name '*.wav'))
	for w in "${WAV_FILES[@]}" 
	do
		mv -v $w $a/48kHz/
	done

	WAV_FILES_48kHz=($(find $a/48kHz -maxdepth 1 -type f -name '*.wav'))
	for wf in "${WAV_FILES_48kHz[@]}" 
	do
		echo $wf
		filename=$(basename "$wf")
		sox $wf -c 1 -r 16000 $a/$filename
	done

done

