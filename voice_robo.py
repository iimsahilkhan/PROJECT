"""import os

if __name__== '__main__':
    print("Welcome to robospeaker 1.1 created by sahil")
    x = input("Enter what you want me to speak")
    command = f"engine.say{x}"
    os.system(command)

import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# convert this text to speech
text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()

# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)"""


#from openai import Engine
# initialize Text-to-speech engine
import pyttsx3
engine = pyttsx3.init()

text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()