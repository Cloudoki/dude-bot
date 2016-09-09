# http://stackoverflow.com/questions/20131689/raspberry-pi-convert-pyaudio-wav-to-flac-48000hz-google-speech

import pyaudio
import signal
import sys
import wave

chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

#open stream
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

all_m = []
data = ''
rel = RATE/chunk

def on_exit(signal, frame):
    print('You pressed Ctrl+C!')
    filename = save_speech(all_m, p)
    stream.close()
    p.terminate()
    sys.exit(0)

def save_speech(data, p):
    filename = 'file'
    # write data to WAVE file
    data = ''.join(data)
    wf = wave.open(filename+'.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
    print "finished saving wav: %s" % filename
    return filename

signal.signal(signal.SIGINT, on_exit)

while (True):
    data = stream.read(chunk)
    all_m.append(data)

print "* listening. CTRL+C to finish manually."
signal.pause()
