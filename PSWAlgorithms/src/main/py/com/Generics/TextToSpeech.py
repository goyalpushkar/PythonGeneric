import os
from gtts import gTTS
from os import path
from playsound import playsound

basepath = path.dirname(__file__)
print(basepath)

generic_resource_path = path.abspath(path.join(basepath, '..', '..', '..', 'resources')) + "/"
print(generic_resource_path)

text_speech = open(generic_resource_path+"ReadFile", "r").read().replace("\n", " ")
TTS = gTTS(text=str(text_speech), lang='en-in')

TTS.save(generic_resource_path+"SpeechFile.mp3")
# os.system(generic_resource_path+"SpeechFile.mp3")
playsound(generic_resource_path+"SpeechFile.mp3")