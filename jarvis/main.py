import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning boss!")
    elif hour>= 12 and hour <18:
        speak("Good Afternoon boss!")
    else:
        speak("Good Evening boss!")

    speak("I am Friday Any help?")

def takeCommand():
    #! it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return 'None'
    return query
    

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com",'your-password')
    server.sendmail("youremail@gmail.com",to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

    #! logic for executing tasks based on query
    if 'wiikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences = 2)
        speak('According to wikipedia')
        print(results) 
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\aakas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'send email to aakash' in query:
        try:
            speak("What should i say")
            content = takeCommand()
            to = 'aakashgawde21@gmail.com'
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry boss,i am not able to send this email")