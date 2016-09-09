#!/bin/bash

echo "Recording… Press Ctrl+C to Stop."

./speech2text.sh

QUESTION=$(cat stt.txt)
echo "Me: ", "$QUESTION"

ANSWER=$(python queryprocess.py "$QUESTION")
echo "Robot: ", "$ANSWER"

python tts.py "$ANSWER"
