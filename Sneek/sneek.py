#███████╗███╗   ██╗███████╗███████╗██╗  ██╗
#██╔════╝████╗  ██║██╔════╝██╔════╝██║ ██╔╝
#███████╗██╔██╗ ██║█████╗  █████╗  █████╔╝ 
#╚════██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔═██╗ 
#███████║██║ ╚████║███████╗███████╗██║  ██╗
#╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝ 


import pyttsx3, datetime, json, requests, base64, subprocess, random
import speech_recognition as sr
from colorama import Fore
from os import system
from sys import platform
from plyer import notification
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():        
    print(Fore.RED + "╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│    Hello I'm sneek your virtual assistant      │")
    print("│           How can I help you ?                 │")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    speak("Hello I'm sneek your virtual assistant, How can I help you?" + Fore.RESET)
    notification.notify(
        title='Sneek Started',
        message='Sneek virtual Assistant Online'
    )

def help():
    if platform == "linux" or platform == "linux2":
        clear = lambda: system('clear')
    elif platform == "win32":
        clear = lambda: system('cls')
    clear()
    print(Fore.RED + ("""
[!] help     -> shows this message
[!] system   -> to run system commands
[!] about    -> gives you information about sneek
[!] version  -> gives you the sneek version
[!] shutdown -> shuts down sneek
[!] clear    -> clears terminal
[!] notepad  -> opens new notepad
[!] datetime -> shows current date and time
[!] restart  -> restarts the virtual assistant
[!] code     -> starts vs code
[!] quote    -> gives you the quote of the day
[!] custom   -> give you a tutorial on how to add custom commands
    """))
    notification.notify(
        title='',
        message=f'Check your terminal'
    )

def about():
    speak("Sneek is a basic virtual assistant writen in python3")

def version():
    link    = "https://pastebin.com/raw/qrutdV7x"
    r       = requests.get(link)
    version = r.text
    notification.notify(
        title='',
        message=f'{version}'
    )

def run_system_command():
    speak("What command")
    command = take_cmd().lower()
    system(command)
    notification.notify(
        title='',
            message=f'[+] Command {command} successfully ran'
    )


def notepad():
    subprocess.run('notepad', shell=True)

def date_time():
    date_time = datetime.now()
    dt        = date_time.strftime("%d/%m/%Y %H:%M:%S")
    notification.notify(
        title='Current date and time',
            message=f'Todays Date & time-> {date_time}\n'
    )

def restart():
    notification.notify(
        title='',
        message=f'Restarting'
    )
    system("python3 sneek.py")

def code():
    subprocess.run('code', shell=True)

def qod():
    link = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
    r    = requests.get(link)
    q    = r.json()
    qod  = q['thought']["quote"].strip()
    notification.notify(
        title='Quote of the day',
        message=f'{qod}'
    )
    print(f"[+] {qod}")

def custom_tut():
    if platform == "linux" or platform == "linux2":
        clear = lambda: system('clear')
    elif platform == "win32":
        clear = lambda: system('cls')
    clear()
    print(Fore.RED + """
    [1] make a function of what you want the command to do
    [2] go to the bottom of sneek.py where it has all the ifs and elifs and add your command
    [3] example -> if "test" in command: test()
    """)

def take_cmd():
    global listen
    r = sr.Recognizer()
    query = ""
    listen = True
    while listen is True:
        with sr.Microphone() as source:
            print(Fore.GREEN + "[+] Listening.....")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio = r.listen(source, timeout=20, phrase_time_limit=10)
        try:
            print("[+] Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"[+] User said -> {query}")

        except sr.UnknownValueError:
            print(Fore.RED + "[x] I didn't get it...what was that..")
        except sr.RequestError:
            speak(Fore.RED + "[x] Sorry sir I didn't get that.")
        except KeyboardInterrupt:
            pass
        except Exception as ie:
            print(ie)
            speak(Fore.RED + "[x] Say that again please...")
            return "None"
        return query


if __name__ == '__main__':
    if platform == "linux" or platform == "linux2":
        clear = lambda: system('clear')
    elif platform == "win32":
        clear = lambda: system('cls')
    clear()
    welcome()

try:
    while True:
        command = take_cmd().lower()

        if "help" in command:
            help()
        elif "close" in command or "exit" in command or "shutdown" in command:
            print("[+] Shutting down" + Fore.RESET)
            notification.notify(
                title='',
                message='Shutting down, Sneek offline'
                )
            break
        if "about" in command:
            about()
        elif "clear" in command:
            clear()
        elif "version" in command:
            version()
        if "system" in command:
            run_system_command()
        elif "notepad" in command:
            notepad()
        if "what's the time" in command:
            date_time()
        elif "restart" in command:
            restart()
        if "code" in command:
            code()
        elif "quote" in command:
            qod()
        if "custom" in command:
            custom_tut()

except Exception as e:
    print(e)