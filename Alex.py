import requests
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import sys
from os import startfile, system
import time
import pyjokes
import pyautogui
import randfacts
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import feedparser
import os
import time
from core import speak, takecommand
from tkinter import ttk, scrolledtext
import tkinter as tk
import threading
from openai import OpenAI



# AI mode
def ai():
    try:
        speak("Yes sir! how can I help you.. ")

        while True:
            vm=takecommand().lower()

            if any(word in vm for word in ["exit", "stop", "quit", "cancel"]):
                speak("Okay sir, exiting AI mode.")
                break

            else:
                client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key="Enter_Your_API_KEY",
                )

                completion = client.chat.completions.create(

                extra_body={},
                model="deepseek/deepseek-r1:free",
                messages=[
                    {
                    "role": "user",
                    "content": f"{vm}\n\nPlease keep the response short, not more than 3 lines."
                    }
                ]
                )
                speak(completion.choices[0].message.content)

        #retry function..
        speak("Do you want to retry the AI mode sir..")
        dm=takecommand().lower()
        if dm=='yes':
            ai()
        else:
            speak("OK. switching to normal mode.")

    except Exception as e:
        print(e)



# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good morning sir, its {tt} ")
    elif hour>=12 and hour<18:
        speak(f"Good afternoon sir, its {tt} ")
    else:
        speak(f"Good evening sir, its {tt}")

    api_key = "5b05f27203f3f2d2ecd6efe6f9db0bf7"  # Replace with your API key
    city = "Siliguri"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        speak(f"Current temperature in {city} is {int(temp)-1}°C")
    else:
        data = response.json()
        temp = data["main"]["temp"]
        speak(f"Current temperature in {city} is {temp}°C")
            
    speak("I am Alex. Please Tell Me Sir How can I Help You ?")

# to get the weather forcast
def weather(city):
    api_key = "5b05f27203f3f2d2ecd6efe6f9db0bf7"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        speak(f"The weather in {city} is {weather} with a temperature of {int(temp)-1}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.")
    else:
        speak(f"Sorry, couldn't fetch weather data for {city}.")


# for news updates
def news():
    speak("Sir, what kind of news would you like to know? (e.g., technology, sports, business)")
    
    news_type = takecommand().lower()
    rss_url = f"https://news.google.com/rss/search?q=India+{news_type}&hl=en-IN&gl=IN&ceid=IN:en"
    
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    day = ["first", "second", "third"]
    head = [entry.title for entry in feed.entries[:len(day)]] # using list comprehension to get the top 2 headline
    if not head: # if no headlines found
        speak(f"Sorry, I couldn't find any {news_type} news right now.")
        return

    # Read out the top 3 headlines
    for i in range(len(head)):
        speak(f"Today's {day[i]} news is: {head[i]}")


# pdf reader
def pdf_reader():
    book = open("c:\\User\\ADMIN\\Downloads\\23.pdf")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in book {pages} ")
    speak("sir please enter the page number I have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


# main logic   
def run_alex():

    wish()# to greet the user

    while True:

        query = takecommand().lower() # to take command
        
        # logic building for tasks(Main codding)
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("opening notepad...")
            os.startfile(npath)
        elif "close notepad" in query:
            speak("okya sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open python" in query:
            apath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
            os.startfile(apath)
        elif "close python" in query:
            speak("okya sir, closing python")
            os.system("taskkill /f /im python.exe")

        elif "open pdf maker" in query:
            dpath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32"
            os.startfile(dpath)
        elif "close pdf maker" in query:
            speak("okya sir, closing notepad")
            os.system("taskkill /f /im AcroRd32.exe")

        elif "open powerpoint" in query:
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(cpath)
        elif "close powerpoint" in query:
            speak("okya sir, closing powerpoint")
            os.system("taskkill /f /im Microsoft PowerPoint 2010.exe")

        elif "open ms office" in query:
            epath = "C:\\Users\\ADMIN\\Desktop\\Microsoft Office"
            os.startfile(epath)
        elif "close ms office" in query:
            speak("okya sir, closing ms office")
            os.system("taskkill /f /im Microsoft Office.exe")

        elif "open excel" in query:
            fpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010"
            os.startfile(fpath)
        elif "close excel" in query:
            speak("okya sir, closing excle")
            os.system("taskkill /f /im Microsoft Excel 2010.exe")

        elif "open wordpad" in query:
            gpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\WordPad"
            os.startfile(gpath)
        elif "close woardpad" in query:
            speak("okya sir, closing woardpad")
            os.system("taskkill /f /im WordPad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")
        elif "close notepad" in query:
            speak("okya sir, closing cmd")
            os.system("taskkill /f /im cmd.exe")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play song" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org/').text
            speak(f"your ip address is {ip}")

        elif "open wikipedia" in query:
            speak("opening wikipedia...")
            query = query.replace("wikipedia","")
            speak("what to search on wikipedia")
            ay = takecommand().lower()
            results = wikipedia.summary(f"{ay}", sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            speak("opening facebook...")
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            speak("opening instagram...")
            webbrowser.open("www.instagram.com")

        elif "open whatsapp" in query:
            speak("opening whatsapp...")
            startfile("C:\\Users\\ADMIN\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        elif "close whatsapp" in query:
            speak("okya sir,closing whatsapp")
            os.system("taskkill /f /im WhatsApp.exe")


        elif "open zoom" in query:
            speak("opening zoom...")
            webbrowser.open("www.zoom.com")

        elif "open google meet" in query:
            speak("opening google meet...")
            webbrowser.open("www.google meet.com")

        elif "open telegram" in query:
            speak("opening telegram...")
            startfile("C:\\Users\\ADMIN\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        elif "close telegram" in query:
            speak("okya sir,closing telegram")
            os.system("taskkill /f /im Telegram.exe")

        elif "open filmora" in query:
            speak("openin filmora...")
            startfile("C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe")
        elif "close filmora" in query:
            speak("okya sir,closing filmora")
            os.system("taskkill /f /im Wondershare Filmora X.exe")

        elif "open scratch" in query:
            speak("opening strach...")
            startfile("C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Scratch 3\\Scratch 3.exe")
        elif "close scratch" in query:
            speak("okya sir,closing scratch")
            os.system("taskkill /f /im Scratch 3.exe")



        elif "open gmail" in query:
            speak("opening gmail...")
            webbrowser.open("www.gmail.com")

        elif "open flipkart" in query:
            speak("opening flipkart...")
            webbrowser.open("www.flipkart.com")

        elif "open google" in query:
            speak("opening google...")
            speak("sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play music in youtube" in  query:
            speak("playing music on youtube...")
            speak("what song would you like to listen sir?")
            dm = takecommand().lower()
            speak("playing it for you sir..")
            pywhatkit.playonyt(f"{dm}")
            

        elif "tell me a story" in query:
            speak("Story Starting...")
            speak("An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.The longer he lived, the more bile he was becoming and the more poisonous were his words. People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him.He created the feeling of unhappiness in others.But one day, when he turned eighty years old, an incredible thing happened. Instantly everyone started hearing the rumour:An Old Man is happy today, he doesn’t complain about anything, smiles, and even his face is freshened up.The whole village gathered together. The old man was asked:Villager: What happened to you?Nothing special. Eighty years I’ve been chasing happiness, and it was useless. And then I decided to live without happiness and just enjoy life. That’s why I’m happy now.")
            speak("The story tell us that:Don’t chase happiness. Enjoy your life.")

        

        # to tell jokes
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os,system("shutdown /r /t 5")

        elif "no please exit" in query:
            speak("okay sir, I am shutting down")
            speak("thankyou sir for using me, have a good day!")
            sys.exit()

        elif "window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "news" in query:
            speak("Please wait sir, feteching the latest news")
            news()

        elif "facts" in query:
            a = randfacts.getFact()
            b = randfacts.getFact()
            c = randfacts.getFact()
            
            x = a, b, c, 
            facts = ("one", "tow", "three")
            for i in range (len(facts)):
                speak(f"Fact number {facts[i]}, {x[i]}")

        elif "where i am" in query or "wher we are" in query:
            speak("wait sir let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org/").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                geo_requests = requests.get(url) 
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state'] 
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass

        elif "pdf" in query: # not working
            pdf_reader() 

        elif "file" in query or "hide all folderr" in query:
            speak("sir plese tell you want to hide all file or make it visbale for everyone")
            condition = takecommand().lower()
            if "make it hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir all the file in this folder are hidden now")

            elif "make it visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir all the files are visible now")

            elif "leave it" in condition:
                speak("ok sir..")


        elif "temperature" in query or "weather" in query:
            speak("Which city would you like to know the weather of?")
            city = takecommand().lower()
            weather(city)
            

        elif "activate" in query:
            # from pywikihow import search_wikihow
            speak("mod activated..")
            while True:
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okya sir,mod is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                        
                except Exception as e:
                    speak("sorry sir i am not able to find this")

        elif "how are you" in query:
                speak("I am fine sir, what about you?")
                takecommand()

        elif "hello" in query:
                speak("Hello sir I am Alex,An Virtual Robot, What Can I do For you?")
                takecommand()

        elif "what can you do for me" in query:
            speak("I can perform these following action:")
            speak("Sir I can Play Music for you")
            speak("I can search anything for you by the command(Open Google or by Opening Wikipedia)")
            speak("I can tell news and facts")
            speak("I can tell jokes for you to change your your mood")
            speak("I can tell story for you")
            speak("I can able to forecast weather")
            speak("I can do all the basic thing that you want like openig whatsapp,instagram,facebook,gmail,microsoft office and lots of thing i am able to do sir.")
            speak("Sir now say that what can i do for you")

        elif "not now" in query:
            speak("okya sir can I shut down my self")
            if "yes" in takecommand():
                speak("thankyou sir for using me, have a good day!")
                sys.exit()


        elif "wait" in query or "weight" in query:
            speak("For how many seconds do I have to wait sir?")
            user=takecommand()
            user=int(user.split(" ")[0])
            speak("okay sir, I am waiting for you")
            time.sleep(user)

        elif "take a note" in query:
            # speak("Tell me the note sir..")
            # note=takecommand()
            # print(note)
            # speak("Do i have to save it sir?")
            # n=takecommand().lower()
            # n=n.split(" ")[0]
            speak("Tell me the note sir..")
            note=takecommand().lower()
            print(note)

            while True:
                speak("Do i have to save it sir?")
                n=takecommand().lower()
                n=n.split(" ")[0]

                if n=="yes":
                    speak("tell me the name of the file..")
                    sv=takecommand().lower()
                    speak("file saved..")
                    with open(f"{sv}.txt","w") as f:
                        f.write(note)
                        break   

                elif n == "no":
                    print("Ok sir..")
                    break

                else: 
                    pass

        elif "switch to" in query:
            speak("Switching to AI mode sir..")
            ai()
        
        else:
            pass


        speak("sir, do you have any other work")
 
        
# to run alex
if __name__ == "__main__":
    run_alex()


# ----- GUI setup------

# # GUI Setup
# def create_gui():
#     global response_label
#     window = tk.Tk()
#     window.title("Alex - Virtual Assistant")
#     window.geometry("500x400")
#     window.config(bg="#282c34")

#     title_label = tk.Label(window, text="Welcome to Alex", font=("Helvetica", 16, "bold"), fg="white", bg="#282c34")
#     title_label.pack(pady=20)

#     response_label = tk.Label(window, text="", font=("Helvetica", 14), fg="yellow", bg="#282c34")
#     response_label.pack(pady=30)

#     start_button = tk.Button(window, text="Start Alex", font=("Helvetica", 14), command=run_alex, bg="#4caf50", fg="white", relief="solid")
#     start_button.pack(pady=20)

#     window.mainloop()

# if __name__ == "__main__":
#     create_gui()



   
