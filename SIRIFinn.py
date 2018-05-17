import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
import time

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Hello there, how are you doing? I am pretending to be Siri. Do you think I sound like her?")

siriquestion = pg.prompt("Do I sound like Siri")

if siriquestion == "Yes":
    speak.Speak("Thank you! What's your name?")

else:
    speak.Speak("That is not nice. Can you not be more encouraging? What's your name?")

answer = pg.prompt("Enter your name")

speak.Speak("Hello " + answer + ", nice to meet you. What's your favourite food?")

food = pg.prompt("Enter your favourite food.")

speak.Speak("I don't like " + food + ". In fact, I don't like any food. I like to consume electricity and user information.")

speak.Speak("What video would you like to watch?")

video = pg.prompt("Enter your video below.")

speak.speak("Ok, let's look for " + video + " on YouTube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
