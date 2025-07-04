import pyttsx3
import datetime
import webbrowser
import wikipedia
import calendar
import speech_recognition as sr
import keyboard 
import pywhatkit
from tkinter import *
from PIL import Image, ImageTk
import pyjokes
import ctypes

root = Tk()
root.geometry('1920x1080')
img = (Image.open("background.jpg"))
resized_img = img.resize((1920,1080), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized_img)
cnvs = Canvas(root, height=1080, width=1920)
cnvs.create_image(0,0, image = img, anchor = NW)
cnvs.create_text(1600,200, text="Voice Assistant by \nC Hemachandra\nSuhas\nHarsha\nAniruddha", font=("Times New Roman", 24), fill="white")
cnvs.place(relx = 0, rely=0)


def execute():
    def speak(audio):
        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        
        engine.say(audio)
        
        engine.runAndWait()
    def Take_query():

        Hello()
        
        while(True):
            
            query = takeCommand().lower()

            if "tell me your name" in query:
                speak("I am Alexa. Your desktop Assistant")
                continue

            
            elif "who made you" in query or "who created you" in query:
               speak("I have been created by Hemachandra")
               continue 

            elif 'the time' in query:
              strTime = datetime.datetime.now()  
              speak(f"Sir, the time is {strTime}")
              continue

            if "open youtube" in query:
                speak("opening youtube ")
                webbrowser.open("www.youtube.com")
                continue

            elif 'joke' in query:
                 speak(pyjokes.get_joke())
                 continue

            if 'wikipedia' in query:
              speak('Searching Wikipedia...')
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences = 2)
              speak("According to Wikipedia")
              print(results)
              speak(results)
              continue
                        

            elif "open google" in query:
                speak("Opening Google ")
                webbrowser.open("www.google.com")
                continue

            elif "play" in query:
                song = query.replace('play','')
                speak('playing'+song)
                pywhatkit.playonyt(song)
                continue

            elif"i love you" in query:
                speak("i love you too dear")
                continue

            elif "open amazon" in query:
                speak("opening amazon")
                webbrowser.open("www.amazon.com")
                continue

            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                continue


            elif "thank you" in query:
                speak("Bye. if you are intrested please update me...take care..")
                exit()


    def takeCommand():

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening')
            
            r.pause_threshold = 0.7
            audio = r.listen(source)
        
            try:
                print("Recognizing")
                
                Query = r.recognize_google(audio, language='en-in')
                print("the command is printed=", Query)
                
            except Exception as e:
                print(e)
                print("Say that again sir")
                return "None"
            
            return Query

    def tellTime(self):

        time = str(datetime.datetime.now())
        
        speak(time)
        hour = time[11:13]
        min = time[14:16]
        self.Speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")	
    """
    This method will take time and slice it "2020-06-05 17:50:14.582630" from 11 to 12 for hour
    and 14-15 for min and then speak function will be called and then it will speak the current
    time
    """
    def Hello():
        speak("hello sir I am your desktop assistant Tell me how may I help you")
    if __name__ == '__main__':
        Take_query()


btn = Button(text="Activate", command=execute)
btn.configure(font=("Times New Roman",24))
btn.place(relx = 0.75, rely=0.75, anchor = CENTER)

root.mainloop()