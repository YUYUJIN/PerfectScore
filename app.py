import threading
from module.player import player
from module.recorder import recorder
from module.scoring import ms

if __name__=='__main__':
    MRplayer=player()
    AudioRecorder=recorder()
    mainScore=ms()

    playerThread=threading.Thread(target=MRplayer.run,args='')
    recorderThread=threading.Thread(target=AudioRecorder.run,args='')
    mainThread=threading.Thread(target=mainScore.run,args=(MRplayer,AudioRecorder))

    playerThread.start()
    recorderThread.start()
    mainThread.start()
