#get a interger number from the user and pass it to the function called findevenorodd(). 
# Let the function print whether the number is even or odd.

def findevenorodd(val):
    if(val%2==0):
        print("The value ",val," is even")
    else:
        print("The value",val,"is odd")

val=int(input("Enter the values to check even or odd: "))
findevenorodd(val)
