import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import smtplib # Simple Mail Transfer Protocol
import time

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', 'google secret password') #you can get it from google account, private application.
    server.sendmail('abc@gmail.com', to, content)
    server.close()

# def setTimer(minutes):
#     seconds = minutes * 60
#     say(f"Setting a timer for {minutes} minutes.")
#     time.sleep(seconds)
#     say("Timer complete. Time's up!")

if __name__ == '__main__':
    print("J.A.R.V.I.S ACTIVATED")
    say("I am Jarvis, Sir. Please tell me how may I help you?")
    while True:
        print("Listening...")
        query = takeCommand()
        if "How are you".lower() in query.lower():
            say("I am good! What can I do for you? ")
            
        if "Open Youtube".lower() in query.lower():
            webbrowser.open("https://www.youtube.com/")
            say("Opening Youtube Smith.")

#Can be implemented for more web applications, and to make shorter using 
#Dictionary, and iterating to match the keyword with the values which will store the link.

        # if "set timer" in query:
        #     try:
        #         say("For how many minutes?")
        #         timer_minutes = takeCommand()
        #         min = int(timer_minutes)
        #         setTimer(timer_minutes)
        #     except ValueError:
        #         say("Invalid input for minutes. Please try again.")

        if "time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"It is {hour} {min}")

        if 'open whatsapp'.lower() in query.lower():
            os.system(f"open /Applications/WhatsApp.localized/WhatsApp.app")
        elif 'send email' in query:
            try:
                say("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"    
                sendEmail(to, content)
                say("Email has been sent!")
            except Exception as e:
                print(e)
                say("Sorry Smith. I am not able to send this email")
        
        elif 'thank you' in query:
            break