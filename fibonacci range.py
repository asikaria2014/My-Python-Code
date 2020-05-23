upto = int(input("enter a number and I will show numbers of fibonacci series upto that number "))

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
        if (c >= upto):
            break
else:
    print("Positive numbers only please")
