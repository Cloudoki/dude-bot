# http://stackoverflow.com/questions/20131689/raspberry-pi-convert-pyaudio-wav-to-flac-48000hz-google-speech

import pyaudio

chunk = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
THRESHOLD = 525 #The threshold intensity that defines silence signal (lower than).
SILENCE_LIMIT = 3 #Silence limit in seconds. The max ammount of seconds where only silence is recorded. When this time passes the recording finishes and the file is delivered.

#open stream
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print "* listening. CTRL+C to finish manually."
all_m = []
data = ''
rel = RATE/chunk
slid_win = deque(maxlen=SILENCE_LIMIT*rel)
started = False

while (True):
    data = stream.read(chunk)
    slid_win.append (abs(audioop.avg(data, 2)))

    if(True in [ x>THRESHOLD for x in slid_win]):
        if(not started):
            print "starting record"
        started = True
        all_m.append(data)
    elif (started==True):
        print "finished"
        #the limit was reached, finish capture and deliver
        filename = save_speech(all_m, p)
        started = False
        #slid_win = deque(maxlen=SILENCE_LIMIT*rel)
        #all_m= []
        stream.close()
        p.terminate()
        return


def save_speech(data, p):
    filename = 'file'
    # write data to WAVE file
    data = ''.join(data)
    wf = wave.open(filename+'.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(48000)
    wf.writeframes(data)
    wf.close()
    print "finished saving wav: %s" % filename
    return filename
