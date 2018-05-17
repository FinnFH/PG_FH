name = "Finn"

subjects = ["English", "Math", "Science", "Latin", "History"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

countries = ["Germany", "South Africa", "Canada", "Great Britain", "Spain", "France", "Mexico", "China", "Indonesia", "Argentinia"]

for i in countries:
    if i in ["Germany", "South Africa", "Canada", "Great Britain", "Spain"]:
        print( i + " is a country.")
    else:
        print("I have not been to " + i + " but I want to travel there.")

movies = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favourite movies is " + i)
