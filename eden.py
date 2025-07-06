# eden.py
import os
import time
import json
from gtts import gTTS
import sounddevice as sd
import scipy.io.wavfile as wav
from command_handler import handle_command
from text_to_speech import speak
from wake_word import detect_wake_word
from goal_tracker import track_goals
from memory import remember, recall


def play_startup_voice():
    try:
        fs, data = wav.read("Eden_voice.wav")
        sd.play(data, fs)
        sd.wait()
    except Exception as e:
        print("Couldn't play startup voice:", e)


def eden_loop():
    play_startup_voice()
    print("\n🟣 Eden Assistant is online.")
    while True:
        user_input = input("🗣️ You: ")
        if user_input.lower() in ["exit", "quit", "shutdown"]:
            print("🔕 Eden is shutting down.")
            break
        remember(user_input)
        response = handle_command(user_input)
        print(f"🟢 Eden: {response}")
        speak(response)
        track_goals()


if __name__ == "__main__":
    eden_loop()
