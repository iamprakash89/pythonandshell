#### this assesment for checking the loan eligibility
print("this assesment for checking the loan eligibility")
salary=int(input("enter your salary"))
age=int(input("enter your age"))
if(salary>=20000 or age<=25):
    print("you are eligible for loan")
    loan=int(input("enter your loan amount"))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("Maximum amout of loan is 50000")
else:
    print("you are not eliblie for loan")

