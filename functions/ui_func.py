from app import MainWindow
from ui_main import *
import pyttsx3
import speech_recognition as sr

import json
import requests

import os
from PySide6.QtCore import QThread
from PySide6 import QtCore

prompt = ""
tts = ""
stt = ""
isRunning = False

class UIFunc(MainWindow):
    def reply(self):
        global prompt
        prompt = self.ui.inpt.toPlainText() 
        if prompt != "":
            if isRunning == False:
                self.worker = WorkerThread()
                self.worker.reply_generated.connect(self.update_output_label)
                self.worker.start()

                self.ui.output_label.setText("Generating your recipe...")
        

    def speak(self):
        if isRunning == False:
            self.worker = WorkerThread2()
            self.worker.start()
    
    def talk(self):
        if isRunning == False:
            self.worker = WorkerThread3()
            self.worker.reply_generated.connect(self.update_input_label)
            self.worker.start()

            self.ui.inpt.setText("Speak..")

class WorkerThread(QThread):
    reply_generated = QtCore.Signal(str)
    def run(self):
        print("Generating recipe")
        global isRunning
        isRunning = True
        try:
            global prompt, tts
            headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjBiNTNiNmQtNDM4Mi00ZDI1LTk5ZDYtNDA5NWQwMjgzMzNmIiwidHlwZSI6ImFwaV90b2tlbiJ9.QhyEJJ7pJ6BLdS6k15qATwdEB7inecLdNSA6_VWhTio"}

            url = "https://api.edenai.run/v2/text/generation"
            payload = {
                "providers": "openai",
                "text": f'''you are a Virtual Chef and you will give answers to
                only and only the questions about kitchen and food related queries nothing else. 
                if you were asked anything out of the scope of kitchen, food or meal plan related queries you 
                will reply with I can not answer that please ask something kitchen related but if the question is in the scope don't say that and just answer what is being asked.
                also give the total count for macros such as fat, carbohydrates, calories." {prompt}''',
                "temperature": 0.2,
                "max_tokens": 600,
                "fallback_providers": ""
            }

            response = requests.post(url, json=payload, headers=headers)
            result = json.loads(response.text)
            print(result)

            # Check if 'openai' is present in the keys
            if 'openai' in result:
                response = result['openai']['generated_text']
            else:
                print("Key 'openai' not found in the result")

        except Exception as e:
            print(e)
            response = f'''An error occured!
It might be:
1. API issue
2. Internet might not be connected
3. something else went wrong'''

        self.reply_generated.emit(response.lstrip("\n\n"))
        tts = response

        isRunning = False

class WorkerThread2(QThread):
    def run(self):
        global tts
        print("running speech worker")
        global isRunning
        isRunning = True
        engine = pyttsx3.init()

        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) # change index to use a different voice

        # converting text to speech
        engine.say(tts)
        engine.runAndWait()

        isRunning = False

class WorkerThread3(QThread):
    reply_generated = QtCore.Signal(str)
    def run(self):
        global stt
        global isRunning
        isRunning = True
        r = sr.Recognizer()

        # taking input from microphone
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)

        # converting speech to text
        try:
            text = r.recognize_google(audio)
            stt = text
            print("You said: ", text) 
        except Exception as e:
            stt = "Sorry, could not recognize your speech."
            print(f"Sorry, could not recognize your speech. {e}")

        self.reply_generated.emit(stt)

        isRunning = False