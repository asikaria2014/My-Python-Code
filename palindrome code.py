import sys
UserString = input('''Enter your string and I will tell if it is palindrome: ''')
UserString=UserString.lower()
UserStringLen = int(len(UserString))
counter = 0

for BackCounter in range (UserStringLen+1, 1, -1):
    ForwardString = UserString[counter]
    BackwardString = UserString[BackCounter-2]
    counter += 1
    if ForwardString != BackwardString :
        print("\n \n" + UserString + " is not a palindrome \n")
        print ("Program written by Om Sikaria")
        sys.exit()
print( "\n \n" + UserString + " is a palindrome \n")
print ("Program written by Om Sikaria")
                   


