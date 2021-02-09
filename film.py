films = {"Star Wars":[13,17],
         "Lion King":[4, 12],
         "Game of Thrones":[16, 1],
         "Toy Story":[9, 8]
         }
print(films)

while True:
    choice = input("What would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: "))
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry we are sold out!")
        else:
            print("You are too young to watch the film.")
    else:
        print("We don't have that film")
