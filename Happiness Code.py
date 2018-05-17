import pyautogui as pg
import webbrowser
import time

answer = pg.confirm(text="How do you want to be made happy?", title="Choose your happiness", buttons=['Funny video', 'Cat video', 'Satisfying video'])


if answer == "Funny video":
    question2 = pg.confirm("What kind of funny video?","Choose your funny video",["Funny videos compilation","Fortnite"])
    
    if question2 == "Funny videos compilation":
        webbrowser.open("https://www.youtube.com/user/AFVofficial/videos")
        time.sleep(2)
        i = 0
        while i < 17:
            i += 1
            pg.hotkey("tab")
        pg.hotkey("enter")

    elif question2 == "Fortnite":
        question3 = pg.confirm("What kind of Fortnite video?", "Fortnite video kind",["Fortnite funny moments", "Fortnite skills compilation"])

        if question3 == "Fortnite funny moments":
            webbrowser.open("https://www.youtube.com/results?search_query=fortnite+funny+moments")
            time.sleep(2)
            i = 0
            while i < 7:
                i += 1
                pg.hotkey("tab")
            pg.hotkey("enter")

        elif question3 == "Fortnite skills compilation":
            webbrowser.open("https://www.youtube.com/results?search_query=fortnite+skills+compilation")
            time.sleep(2)
            i = 0
            while i < 7:
                i += 1
                pg.hotkey("tab")
            pg.hotkey("enter")

elif answer == "Cat video":
    webbrowser.open("")

      
            
