import pyautogui as pg
import time
import webbrowser

#Ravenclaw: 1
#Griffindor: 2
#Slytherin: 3
#Huffflepuff: 4



points = 0

#question 1
answer = pg. prompt(
"""
You have an essay due in a week. What do you do?

a) Who cares about school? You go outside and hope to copy it from your smart friends.
b) You work on one paragraph. You like to work in bits.
c) You are already done with it but check over it a few times.
d) You do it at a normal speed but when you're done, you don't look at it again. 

"""
    )
#give points

if answer == "a":
    points += 2
elif answer == "b":
    points += 3
elif answer == "c":
    points += 1
elif answer == "d":
    points += 4


#question 2
answer = pg. prompt(
"""
Which would you rather do?

a) Read a book
b) Go outside and play sports
c) Play a game with one of your friends
d) Do your homework

"""
    )
#give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


#question 3
answer = pg. prompt(
"""
You see two boys talking. One of them begins to beat the other one up. What do you do?

a) You immedietly go in and try to seperate them
b) You jump in and attack the bully
c) You carefully walk away and tell nooone about it
d) You walk away but then brag to your friends how you beat the bully up.

"""
    )
#give points

if answer == "a":
    points += 4
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1
elif answer == "d":
    points += 3


#question 4
answer = pg. prompt(
"""
Your friend asks you if you want to watch the new movie. Another friend has already asked you to come over. What do you?

a) You tell the second friend that you are of course going to the movies. You tell the other friend that your mom did not allow you to come.
b) You tell both friends that you can't come because you have to study for the test tommorow.
c) Tell the first friend that you have already something to do 
d) Do your homework

"""
    )
#give points

if answer == "a":
    points += 3
elif answer == "b":
    points += 1
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
