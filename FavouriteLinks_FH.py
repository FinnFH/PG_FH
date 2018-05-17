import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=xsS_Fo-jOOw", "https://www.youtube.com/watch?v=du5SopfbML0","https://www.youtube.com/watch?v=Pd3_4Z2tbFU"]

school = ["https://www.drive.google.com", "https://www.classroom.google.com", "https://www.mail.gooogle.com"]

answer = pg.prompt(

"""
Which would you rather do?

a) Youtube
b) School

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in school:
        webbrowser.open(i)
