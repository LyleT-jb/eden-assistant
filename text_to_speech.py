# text_to_speech.py
from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("eden_response.mp3")
    os.system("start eden_response.mp3")