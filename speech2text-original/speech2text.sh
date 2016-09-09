#!/bin/bash

echo "Recording… Press Ctrl+C to Stop."

parecord file.flac --file-format=flac --rate=16000 --channels=1

echo "Processing…"

# Need Google Speech v2 Key
wget -q --post-file file.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com/speech-api/v2/recognize?client=chromium&lang=en_US&key=GOOGLE_SPEECH_KEY" | grep "transcript.*}" | sed 's/,/\n/g;s/[{,},"]//g;s/\[//g;s/\]//g;s/:/: /g' | grep -o -i -e "transcript.*" | cut -d '' -f12 > stt.txt

echo -n You Said:
cat stt.txt

rm file.flac > /dev/null 2>&1
