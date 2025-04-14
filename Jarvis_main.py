import pyttsx3
import speech_recognition
import webbrowser
import datetime 
import os 
import pyautogui
import keyboard

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")   
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")    
        return "None"
    return query 

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile(r"C:\Users\ahmed\OneDrive\Desktop\Jarvis-30\alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:  
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break
                
                elif "Hello" in query:
                    speak("Hello sir, how are you ?")
                elif "I am fine" in query:
                    speak("That's great sir")
                elif "How are you" in query:
                    speak("Perfect sir")
                elif "Thank you" in query:
                    speak("You are Welcome sir") 
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")  
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up ,sir")
                    volumeup()
                    from keyboard import volumedown 
                    speak("Turning volume down ,sir")
                    volumedown()
                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "temperature" in query:
                    search = "temperature in Mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    webbrowser.open(url)
                    speak("Here is the current temperature in Mumbai")
                    
                elif "weather" in query:
                    search = "temperature in Mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    webbrowser.open(url)
                    speak("Here is the current temperature in Mumbai")  
                    
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")  
                    speak("Set the time")
                    a = input("Please tell the time:- ")
                    alarm(a)
                    speak("Done,sir")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir , the time is {strTime}")
                    
                elif "finally sleep" in query:
                    speak("Gooing to sleep,sir")
                    exit()
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                
                    
                
                