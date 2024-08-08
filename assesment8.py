#### Mini Calculator ####
number1=int(input("Enter the First number: "))
number2=int(input("Enter the Second Number: "))
option=input("Enter the any one option ADD or SUB or MUL or DIV: ")

if(option=="ADD"):
    print("The addition values is",number1+number2)
elif(option=="SUB"):
    print("The subtraction value is",number1-number2)
elif(option=="MUL"):
    print("The Multiplication  value is",number1*number2)
elif(option=="DIV"):
    print("The Division values is ",number1/number2)
else:
    print("the entered",option,"is not valid")