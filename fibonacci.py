upto = int(input("enter a number and i will tell you that many numbers in the fibonacci series: "))

a = 0
b = 1
c = 1

if (upto>0):
    print(0)
    for i in range(1, upto):
        print(c)
        c = a + b
        a = b
        b = c
else:

    Print ("Positive numbers only please")
