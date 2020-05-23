import random # import the random package
choice = int(random.randint(1,20)) # generates a random number


question= int(input("Enter a number between 1 and 20. \n"))

while choice!=question:
    if question > choice:
         print("too big")
         question= int(input("Enter a number between 1 and 20. \n"))
    elif question < choice:
        print("too small")
        question = int(input("Enter a number between 1 and 20. \n"))
    if choice == question:
        print("You Win")
