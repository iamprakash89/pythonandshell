print("this program is for verifying the input score out of 100")
#### if score is <35="poor student"
#### if score is greater than 35 but <than 70="Average Student"
#### if score is greater than 70="good Student"
number=int(input("Enter the input number: "))
if(number<=35):
    print("Poor Student")
elif(number>35 and number<70):
    print("Average Student")
else:
    print("good Student")