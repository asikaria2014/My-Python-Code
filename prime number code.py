import sys

Marker = "Y"
user = int(input ("Enter a number and I will tell you if it is a prime number \n"))

prime = 2


if user == 1:
    
    print("this is not a prime number")

    
if user == 2:
    
    print("this is a prime number")

    
while user > prime:
    if user % prime == 0:
        print("this isn't prime")
        print("Divisible by: " + str(prime))
        Marker = "N"
        break
    prime += 1
    
if (Marker == "Y"): print("This is prime")
