import librosa
import numpy as np

SAMPLERATE=22050

class ms:
    def __init__(self):
        print('3초 뒤 반주가 나옵니다 노래를 불러주세요.(엔터를 누르면 녹음을 종료합니다)')
    def run(self,MRplayer,AudioRecorder):
        input()
        MRplayer.stop()
        AudioRecorder.stop()
        print('잠시만 기다려주세요.분석을 시작합니다.')
        self.mainSection()

    def mainSection(self):
        origin_path='./module/audiosource/vocals.wav'
        vocal_path='./module/audiosource/temp.wav'

        origin,_=librosa.load(origin_path)
        vocal,_=librosa.load(vocal_path)

        originTable=librosa.feature.chroma_stft(S=np.abs(librosa.stft(origin)),sr=SAMPLERATE).T
        vocalTable=librosa.feature.chroma_stft(S=np.abs(librosa.stft(vocal)),sr=SAMPLERATE).T

        if originTable.shape[0]>vocalTable.shape[0]:
            originTable=originTable[:vocalTable.shape[0]]
        elif originTable.shape[0]<vocalTable.shape[0]:
            vocalTable=vocalTable[:originTable.shape[0]]

        score=0
        for i in range(len(originTable)):
            if self.cos_sim(originTable[i],vocalTable[i])>0.7:
                score+=1
        score/=len(originTable)
        print('당신의 점수는 {:3.2f}점입니다.'.format(score*100))
        
    def cos_sim(self,row1,row2):
        if np.linalg.norm(row1)*np.linalg.norm(row2)==0:
            return 0
        return np.dot(row1,row2)/(np.linalg.norm(row1)*np.linalg.norm(row2))