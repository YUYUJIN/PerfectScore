import pyaudio
import wave
import time

CHUNK = 1024

class player():
    def __init__(self):
        self.MRsource = wave.open('./module/audiosource/accompaniment.wav', 'rb')
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.p.get_format_from_width(self.MRsource.getsampwidth()),
                        channels=self.MRsource.getnchannels(),
                        rate=self.MRsource.getframerate(),
                        output=True)

        self.data = self.MRsource.readframes(CHUNK)
        self.shutdown=False
    def run(self):
        time.sleep(3)
        while self.data != '':
            if self.shutdown:
                break
            self.stream.write(self.data)
            self.data = self.MRsource.readframes(CHUNK)
    def stop(self):
        self.shutdown=True
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()