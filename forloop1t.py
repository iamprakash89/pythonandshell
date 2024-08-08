#### write a program read 10 numbers and find the sum and average
a=[]    #####>>>>>>> LIST
print("Enter your 10 number")
for i in range(10):
    num=int(input("enter "+str(i+1)+" value: "))  #### here casting is done, converted the int value to strin
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print("The sum of: ",sum)