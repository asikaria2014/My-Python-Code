prime_from = int(input ("Enter the starting number in the range: "))

prime_to = int(input ("Enter the ending number in the range: "))

if prime_from > 1:
    
    for n in range(prime_from,prime_to):

        for i in range(2,n):
           if ( n % i) == 0:
               break
        else :
            print( str(n) + " " )
else:
    print(" 0, 1 and negative numbers are not allowed to be entered")
    
