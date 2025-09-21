import PyBass as pyb
import os.path as path
from os import _exit as exit
def ConvertToUTF8(text : str):
    return text.encode("utf-8") # Encoding UTF-16(Default) to UTF-8 for Working PyBass(Library from ME)

def PlayMusic_AlanWalkerForce():
    bass = pyb.bass
    bass.BASS_INIT(device=-1, freq=44800, flags=0, win=0, dsguid=0)
    if(path.exists("Force.mp3")):
        bass.BASS_START()
        stream = bass.BASS_StreamCreateFile(mem=0, filename=ConvertToUTF8("Force.mp3"), offset=0, length=0, flags=0x4)
        bass.BASS_ChannelPlay(stream, False)
    else:
        exit(3216)