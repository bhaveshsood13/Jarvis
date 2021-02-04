import pyttsx3
from pyttsx3.drivers import sapi5
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   
def wishMe():
   hour=int(datetime.datetime.now().hour)
   if hour<=12 :
      speak("Good Morning!")
   elif hour<18 :
      speak("Good Evening")
   elif hour <24 :
      speak("Good Night!")
   speak("JAARVIS here ...COMMAND me");

def takeCommand():
   '''
   It takes microphone input from the user and returns string output:
   '''
   r=sr.Recognizer()
   with sr.Microphone() as source :
      print("Listening.....")
      r.pause_threshold=0.6
      r.energy_threshold=900
      audio= r.listen(source)

   try:
      print("Recognizing...")
      query=r.recognize_google(audio,language='en-in')
      print(f"User said: {query}\n")
   
   except Exception as e:
      # print(e)
      print("Say that again please....")
      return "None"
   return query

def sendEmail(to ,content):
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login("enter: sender's email id here",'enter: password here')
   server.sendmail("enter: sender's email id here",to,content)
   server.close()




if __name__ == "__main__":
   chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

   while True:
      query=takeCommand().lower()
      

      if 'wikipedia' in query:
         speak("Searching Wikipedia...")
         query= query.replace("Wikipedia","")
         results= wikipedia.summary(query,sentences=1)
         speak("According to Wikipedia")
         print(results)
         speak(results)

      elif 'open youtube' in query:
         webbrowser.get(chrome_path).open_new_tab('youtube.com') 
      elif 'open google' in query:
         webbrowser.get(chrome_path).open_new_tab('google.com') 
      elif 'signals and systems' in query:
         webbrowser.get(chrome_path).open_new_tab('https://classroom.google.com/u/1/c/MTMxODMzMjQ5Mzk2') 
      elif 'exit'  in query:
         speak("Bye bye")
         exit()
         break
      elif 'open this pc' in query:
         path='D:\\'
         path = os.path.realpath(path)
         os.startfile(path);
      elif 'the time' in query :
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak("Sir the time is "+strTime)
      elif 'email to harry' in query:
         try: 
            speak("Enter text")
            content=takeCommand()
            to="bhaveshsood13@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent! ")
         except Exception as e:
            print(e)
            speak("sorry my friend ")

