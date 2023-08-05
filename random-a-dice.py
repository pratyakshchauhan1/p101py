import random
response = input("enter y for yes or enter n for no")
while response == "y":
    no = random.randint(1,6)
    check = int(input("enter a number between 1 to 6"))
    if no == 1 :
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[     ]")
        print("[  00 ]")
        print("[     ]")
        print("[-----]")   
    elif no == 3:
        print("[-----]")
        print("[     ]")
        print("[ 000 ]")
        print("[     ]")
        print("[-----]")   
    elif no == 4:
        print("[-----]")
        print("[     ]")
        print("[0000 ]")
        print("[     ]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[     ]")
        print("[00000]")
        print("[     ]")
        print("[-----]")   
    elif no == 6:
        print("[-----]")
        print("[     ]")
        print("[000000]")
        print("[     ]")
        print("[-----]")   

    if no ==check:
        print("your guessed it right")
    else:
        print("Oops incorect guess")      