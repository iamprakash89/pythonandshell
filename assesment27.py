### get a input a and b and pass it to the fucntion called printrange() let the function print numbers from a to b.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

def printrange(a,b):
    for i in range(a,b):
        print(i)

printrange(a,b)