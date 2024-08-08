print("This program for verify the entered number is divisible by 3 or 5")
number=int(input("Enter the input: "))
if(number%3==0):
    print("The number",number,"is divisible by 3")
elif(number%5==0):
    print("The number",number,"is divisible by 5")
else:
    print("The number",number,"is not duvisible by 3 or 5")


##### using the operator
print("This program for verify the entered number is divisible by 3 and 5")
number=int(input("Enter the input: "))
if(number%3==0 and number%5==0):
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 or 5")