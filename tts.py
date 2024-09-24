import pyttsx3

# initialize the text-to-speech engine
engine = pyttsx3.init()

# set the rate of speech
engine.setProperty('rate', 150)

# set the voice to use
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # change index to use a different voice

# take input text from user
text = input("Enter the text to convert to speech: ")

# convert text to speech
engine.say(text)
engine.runAndWait()
