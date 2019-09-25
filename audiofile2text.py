import speech_recognition as sr
r = sr.Recognizer()
audioFile = sr.AudioFile('OSR_uk_000_0020_8k.wav')
with audioFile as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))