#crating branching here
import os
# import queue
# import threading
import vosk
import json
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def stop():
    engine.stop()

# Initialize Vosk Model
MODEL_PATH = "./model/voice_recognition_model"  # Ensure the 'model' folder is in your project directory
if not os.path.exists(MODEL_PATH):
    print("Vosk model not found! Please download and extract it.")
    exit(1)

vosk_model = vosk.Model(MODEL_PATH)
recognizer = sr.Recognizer()

# Speech recognition function
def recognize_speech():
    mic = sr.Microphone()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening...")

        try:
            audio = recognizer.listen(source)
            audio_data = audio.get_wav_data()
            
            # Use Vosk to recognize speech
            vosk_recognizer = vosk.KaldiRecognizer(vosk_model, 16000)
            if vosk_recognizer.AcceptWaveform(audio_data):
                result = json.loads(vosk_recognizer.Result())
                text = result.get("text", "")
                print(f"You said: {text}")
                
                if text:
                    speak(f"You said: {text}")
                
                return text
        
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that.")

# Example Usage:
if __name__ == "__main__":
    speak("Hello, how can I assist you?")
    print("You said:", recognize_speech())