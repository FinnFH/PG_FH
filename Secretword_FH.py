import random

number = random.randint(0,3)

words = ["Griffindor","Hufflepuff","Ravenclaw","Slytherin", "Hagrid", "Snape", "Dumbledor", "Harry Potter"]
hint1 = ["house","house","house","house", "a character", "a character", "a character", "a character"]
hint2 = ["are brave","are hardworking","are smart","mean", "not a student", "mean", "wise", "brave"]
hint3 = ["red and gold","yellow and black","bronze and blue","green and silver", "small giant", "teacher", "headmaster", "student"]

secretword = words[number]

guess = ""
counter = 0

while True:
    print("Guess the secret harry Potter word")
    print("Type 'type of word', 'character traits', 'additional hints', 'first letter', ot 'give up' for answer.")
    guess = input()

    counter += 1

    if guess == secretword:
        print("You Win!")
        print("It took you " + str(counter) + " guesses.")
        break
    
    elif guess == "type of word":
        print(hint1[number])
        
    elif guess == "character traits":
        print(hint2[number])
        
    elif guess == "additional hints":
        print(hint3[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "give up":
        print("WOOOOOOOOOW! It took you " + str(counter) + " guesses and you still didn't guess it!")

    else:
        print("Guess again.")
