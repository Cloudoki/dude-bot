o "Recording… Press Ctrl+C to Stop."

arecord -D plughw:Twist,0 -vv file.wav --rate=16000 --channels=1

echo "Processing…"

avconv -i file.wav -y -ar 16000 file.flac

speech_key=$(python grab_config.py speech_key)

wget -q --post-file file.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com/speech-api/v2/recognize?client=chromium&lang=en_US&key=$speech_key" | grep "transcript.*}" | sed 's/,/\n/g;s/[{,},"]//g;s/\[//g;s/\]//g;s/:/: /g' | grep -o -i -e "transcript.*" | sed 's/transcript://' |  head -n1 >stt.txt

echo -n You Said:
cat stt.txt

rm file.flac file.wav > /dev/null 2>&1
