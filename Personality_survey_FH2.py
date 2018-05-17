print ("What's your name?")
name = input()

if name == "Finn":
    print("Welcome Back")
else:
    print("Hello " + name)


print("What's your favourite sport?")
sport = input().title

if sport == "hockey":
    print("That's my favourite too!")
elif sport == "soccer":
    print("I love playing soccer too")
elif sport == "tennis":
    print("Meh, I'm not that good at doubles")
elif sport == "Crew":
    print("I really don't like Crew!")
else:
    print(sport + " is fun.")


print("What's your favourite TV show?")
tvshow = input().title

if tvshow == "The Flash":
    print("Who is your favourite character?")
    character = input().title
    if character == "Barry Allen" or character == "The Flash":
        print("Nice, Barry is my favourite character too!")
    else:
        print("I like " + character + "too but my favourite character in Barry Allen.")
else:
    print("I have not watched " + tvshow + "yet. My favourite TV show is The Flash.")

print("What's your favourite book?")
book = input()

if "Harry Potter" in book:
    print("I read all seven books in thirty days. J.K Rowling is a genius! Is she your favourite author?")
    author = input().title
    if "Yes" in author:
        print("Nice, my favourite author is Rick Riordan but J.K Rowling is also a good author.")
    else:
        print("")
elif "Percy Jackson" in book:
    print("I read all five. Is Rick Riordan your favourite author?")
    
