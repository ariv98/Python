import speech_recognition as sp
a=sp.Recognizer()
with sp.Microphone() as source:
    audio=a.listen(source)
try:
    print("you said"+a.recognize_google(audio))
except LookupError:
    print("sry")
