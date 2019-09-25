
import speech_recognition as sr
r = sr.Recognizer()
a=sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=0)
#if you are not sure what index of your microphone is print the variable a.
print("start speaking")
with mic as source:
    #this helps to reduce the noise to certain extent.
    r.adjust_for_ambient_noise(source)
    
    audio1 = r.listen(source)

    try:
        text = r.recognize_google(audio1)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")







