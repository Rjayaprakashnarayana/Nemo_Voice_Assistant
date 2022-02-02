from tkinter import *   # to create GUI Interface of an application
import cv2  # computer vision package related to matlab in python
import PIL.Image
import PIL.ImageTk
import pyttsx3  # used to convert text to speech
import datetime  # used to retrive date and time
import speech_recognition as sr  # used to convert speech to text and give command to Assistant
import pyautogui
import wikipedia   # allows us to search a query supplied as an argument
import webbrowser   # provides a high-level interface to allow displaying Web-based documents to users
import os  # module provides functions for interacting with the operating system
import random  # module to generate random numbers
import pyjokes  # pip install pyjokes To generate some random jokes
# import smtplib
import requests  #  to either retrieve data from a specified URI or to push data to a server
import roman  # helps us convert roman numerals into decimal number and decimal number into roman numerals
import winshell
import ctypes
# from Class1 import Student
# import pytesseract
from PIL import Image
import psutil# pip install psutil
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mridu\AppData\Local\Tesseract-OCR\tesseract.exe"
import sqlite3


numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000} #this dictionary helps to conver numbers in string(alphobetic form) to integer form
a = {'name': 'jayaprakashrayani@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
cwd = os.getcwd()
#'E:\\Newfolder'
window = Tk() #initializing window /pannel object
window.geometry('500x800')
window.iconbitmap(default='favpng_download.ico')
'''
canvas1 = Canvas( window, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")'''

global var
global var1

var = StringVar()
var1 = StringVar()

#to convert text file to voice this function is created
def speak(audio):
    engine.say(audio)#here audio variable refers to string and the text will be converted to audio
    engine.runAndWait()

#this update function is used to refresh / update the Interface
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)
'''
#to send mail we use this function which contains a security less mail id and password
def sendemail(to, content):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587) #we are configuring server with server's IP and port number
    server.ehlo()#------
    server.starttls()
    server.login('18F01A05C0.ansn@apssdc.info@gmail.com','9398697771') # email id - use any email id whose security/privacy is off
    server.sendmail('18F01A05C0.ansn@apssdc.info@gmail.com', to, content)
    server.close()
'''
#to take a screenshot of the entire screen we use this function
def screenshot():
    img= pyautogui.screenshot()
    img.save(cwd +'\\sample.png')#to save the screenshot at D drive
"""This Project Was Done By Anupama and Jaya Prakash Narayana"""
#wishme() is used to wish the user according to the time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning User")
        window.update()
        speak("Good Morning user!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon user!")
        window.update()
        speak("Good Afternoon user!")
    else:
        var.set("Good Evening user")
        window.update()
        speak("Good Evening user!")
    speak("Myself Nemo How may I help you sir") #BotName - Give a name to your assistant
def info():
    speak("I can do multiple tasks for you sir. tell me whatever you want to perform sir")

# to convert speech to text we use this command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query
# to get cpu info we use this function
def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    batrey = psutil.sensors_battery()
    speak("Battrey is at")
    speak(batrey.percent)

def jokes():
    speak(pyjokes.get_joke())#Here we get random jokes from pyjokes library database

# The actual excecution starts here when the user click play button this function starts executing
def play():
    btn2['state'] = 'disabled' #initially buttons are disabled
    btn0['state'] = 'disabled' #initially buttons are disabled
    btn1.configure(bg = 'orange')#here orange represented that our mouse pointer points that particular button
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'about' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open coursera' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir...!')
            window.update()
            speak("Hello Sir How Can I help You")

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia ","")
            result =wikipedia.summary(query,sentences =2)
            speak(result)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")
        
        elif 'screenshot' in query:
            screenshot()
            speak("screenshot has been saved")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'your name' in query:
            var.set("Myself Nemo Sir")
            window.update()
            speak('myself Nemo sir')
        elif "open note" in query or "open notepad" in query or "open editor" in query :
            var.set("Opening Notepad")
            window.update()
            speak('Opening Notepad')
            os.system("Notepad")
        elif 'note' in query:
            speak("What should I remember sir...!")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open(cwd+'\\data.txt','w')
            remember.write(data)
            remember.close()
                   
        elif 'data file' in query:
            textnote = open(cwd+'\\data.txt','r')
            speak("The text note you have is"+textnote.read())
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'who created you' in query:
            var.set('My Creator is Anupama , JayaPrakash and team')
            window.update()
            speak('My Creator is Anupama , JayaPrakash and team')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Nemo')
            window.update()
            speak('Hello Everyone! My self Nemo')
        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" #Enter the correct Path according to your system
            os.startfile(path)
		
        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile('C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit)') #Enter the correct Path according to your system

        elif 'open code blocks' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe") #Enter the correct Path according to your system

        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator") #Enter the correct Path according to your system
        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result'+str(sum))
                    window.update()
                    speak('here is result'+str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit
        
        elif 'student details' in query:
            var.set('Name of the student')
            window.update()
            speak('Name of the student')
            name = takeCommand()
            var.set('standard in which he/she study')
            window.update()
            speak('standard in which he/she study')
            standard = takeCommand()
            var.set('Role Number')
            window.update()
            speak('Role number')
            rollno = takeCommand()
            var.set('Details are saved')
            window.update()
            speak('Details are saved')
        elif 'saved details' in query:
            var.set('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)
            window.update()
            speak('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)

        elif 'selfie' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                #cv2.imshow('pic', frame)
                cv2.imwrite(cwd+'\\selfie.jpg',frame)
            speak('Selfie Saved')
            stream.release()
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter(cwd+'\\output.avi', -1, 20.0, (640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        elif 'CPU info' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "13dcecb6e680450ce143612e9e471c37"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
        ''' elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" #Enter the correct Path according to your system
            os.startfile(path)'''
        
        '''elif 'open pycharm' in query:
            var.set("Openong Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe" #Enter the correct Path according to your system
            os.startfile(path)'''              
label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file=cwd+'\\Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('NEMO')

label = Label(window, width = 300, height = 300)
label.pack()
window.after(0, update, 0)
photo = PhotoImage(file=cwd+'\\abc.png')
photoimage = photo.subsample(2, 2)
photo2 = PhotoImage(file=cwd+'\\def.png')
photoimage2 = photo2.subsample(6,6)
photo3 = PhotoImage(file=cwd+'\\efgh.png')
photoimage3 = photo3.subsample(3,3)
btn0 = Button(image =photoimage3, command = info)
#btn0.grid(row=1,column=0)
btn0.pack()
btn1 = Button(image= photoimage,command = play)
#btn1.grid(row=1,column=1)
btn1.pack()
'''btn1 = Button(text = 'PLAY',image= photo,command = play)
btn1.config(font=("Courier", 12))
btn1.pack()'''
btn2 = Button(image= photoimage2,command = window.destroy)
#btn0.grid(row=1,column=2)
btn2.pack()


window.mainloop()
