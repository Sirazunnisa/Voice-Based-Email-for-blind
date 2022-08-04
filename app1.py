import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import easyimap as e


unm = "mainproject999999@gmail.com"
pwd = "MainProject@1"
r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str1):
    print(str1)
    engine.say(str1)
    engine.runAndWait()

def listen():
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            str1 = "speak Now"
            speak(str1)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                return text
            except:
                str1 = "Sorry could not recognize what have said"
                speak(str1)
def sendmail():
     
    str1 = "Please speak the body of your email"
    speak(str1)
    msg = listen()
    str1 = "you have spoken the message"
    speak(str1)
    speak(msg)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(unm, pwd)
    server.sendmail(unm , rec , msg)
    server.quit()
    str1 = "The mail has been sent"
    speak(str1)

def readmail():
    server = e.connect("imap.gmail.com",unm,pwd)
    server.listids()
    str1 = "please say the serial number of the email you wanna read starting from latest"
    speak(str1)
    a = listen()
    if(a == "Tu"):
    	a = "2"
    b = int(a)-1
    email = server.mail(server.listids()[b])
    str1 = "The email is on: "
    speak(str1)
    speak(email.date)
    
    str1 = "The body of email is : "
    speak(str1)
    speak(email.body)

str1 = "Welcome to voice controlled email service"
speak(str1)

while(1):
	str1 = "what do you want to do?"
	speak(str1)
	str1 = "Speak SEND to send emailSpeak   READ to Read inbox   Speak EXIT to Exit"
	speak(str1)
	ch= listen()
	if(ch=='send' or ch=='sent'):
            str1 = "you have chosen to send an email"
            speak(str1)
            sendmail()
	elif(ch == 'read'):
            str1 = "You have chosen to read email"
            speak(str1)
            readmail()
	

	elif(ch == 'exit'):
             str1 = "You have chosen to exit , see you soon"
             speak(str1)
             exit()
	else:
            str1 = "Invalid choice , you said:"
            speak(str1)
            speak(ch)











	















	











