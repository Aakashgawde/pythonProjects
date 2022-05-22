import os
import pyttsx3

sec = 30
os.system(f"shutdown /s /t {sec}")
pyttsx3.speak(f"Jarvis here sir!,i am shutting down pc in next {sec} session")