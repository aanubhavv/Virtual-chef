import speech_recognition as sr

# initialize the speech recognition engine
r = sr.Recognizer()

# take input from microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

# convert speech to text
try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except:
    print("Sorry, could not recognize your speech.")
