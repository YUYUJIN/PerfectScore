import pyaudio
import numpy as np
import wave
import time
 
CHUNK = 2**10
RATE = 22050

class recorder:
    def __init__(self):
        self.p=pyaudio.PyAudio()
        self.stream=self.p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK,input_device_index=0)
        self.shutdown=False
        self.audioFrames=[]
    def run(self):
        time.sleep(3)
        while(True):
            if self.shutdown:
                break
            data = np.frombuffer(self.stream.read(CHUNK),dtype=np.int16)
            self.audioFrames.append(data)
    def stop(self):
        self.shutdown=True
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.save()
    def save(self):
        wf = wave.open('./module/audiosource/temp.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(self.audioFrames))
        wf.close()
