# Import libraries
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

# Set the word that the audio file triggers on
triggerWord = "gamer"

# Load wii sports audio clip
wiiSports = AudioSegment.from_wav("wiisports.wav")

# Initialize the recognizer, for speech recognition
r = sr.Recognizer()

# Main program loop
while True:
    # Use the microphone for audio input
    with sr.Microphone() as source:
        # Record audio from the microphone, for 5 seconds at a time
        audio = r.record(source, duration=5)

        try:
            # Interpret speech with google
            text = r.recognize_google(audio)
            # If we find the trigger word in the text
            if triggerWord in text:
                print("Trigger detected, playing audio")
                # Play the wii sports audio
                play(wiiSports)
        except sr.UnknownValueError:
            # Do nothing if there isn't any speech detected(program crashes otherwise)
            pass