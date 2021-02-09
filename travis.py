known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Henry"]

while True:
    
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}.Your name recognised".format(name))
        remove = input("Would you like your name to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Good having you by")
    else:
        print("Hmm we have not met yet. ")
        add_user = input("Would you like to be added to our system (y /n)?:").strip().lower()
        if add_user == "y":
            known_users.append(name)
        
        elif add_user == "n":
            print("No worries, see you around!")
        
        
            
              
