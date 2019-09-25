#from PyLyrics import *
#song = PyLyrics.getLyrics("Eminem", "Not Alike")
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
a=sr.Microphone.list_microphone_names()
print("start speaking")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.listen(source)

    try:
        text = r.recognize_google(audio1)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")







