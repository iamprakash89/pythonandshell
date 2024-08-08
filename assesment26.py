### Get the integer mark from user and pass it to the passorfail() function.
### Let the function print mark  the number is pass or fail.

def passorfail(val):
    if(val>=35):
        print("you got the pass mark: ",val)
    else:
        print("you are fail")

val=int(input("Enter your mark to verify you are pass or fail: "))
passorfail(val)