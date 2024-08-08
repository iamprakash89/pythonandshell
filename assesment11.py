print("#############this assesment for get five subject marks and average it")
subject1=int(input("enter the subject1 mark: "))
subject2=int(input("enter the subject2 mark: "))
subject3=int(input("enter the subject3 mark: "))
subject4=int(input("enter the subject4 mark: "))
subject5=int(input("enter yhe subject5 mark: "))
total=subject1+subject2+subject3+subject4+subject5
average=total/5
if(average<35):
    print("additional class required")
else:
    print("you are good to go")