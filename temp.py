## SUM OF FIRST NATURAL NUMBER

def sum_natural(i):
    if i < 0:
        print("enter +ve number")
    else:
        n = 0
        for j in range(1,i+1):
            n += j
    
        print( "sum of first %d natural numbers is %d" %(i, n))
        
sum_natural(int(input("enter any number")))

## PRIME NUMBER
def prime_number(i):
    c = 0
    if i < 0:
        print("enter +ve number")
    elif i == 0:
        print("i don't know")    
    else:
        for j in range(2, i):
            if i % j == 0:
               c=1 
        if c == 1:
            print("Number %d is NOT a PRIME NUMBER" %(i))
        else:
            print("Number %d is PRIME NUMBER" %(i))         

prime_number(int(input("Enter any number")))


## FACTORIAL 
def factorial(i):
    fact = 1
    if i == 0:
        print(1)
    elif i < 0:
        print("Enter a Positive number")    
    else:
        for j in range(1,i+1):
            fact *= j
        print("factorial =", fact)


factorial(int(input("enter any number")))            


## FABONACCI SERIES
def fabonacci(i):
    a = 0
    b = 1
    c = 0
    d = [a, b]
    if i <= 0:
        print("enter +ve integer")
    elif i == 1:
        print(a)
    elif i == 2:
        print(d)
    else:
        for j in range (3, i+1):
            c= a+b
            a = b
            b = c
            d.append(c)
            j = j+1
        print("fabonacci series =" , d)
     
fabonacci(int(input("enter any number")))

##
a = dict{ 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 
         7 : "seven", 8 : "eight", 9 : "nine", 0 : "zero"}
?dict
