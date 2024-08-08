#### wrie program to display n terms of natural numbers and theie sum , test data 7

natrual=[]
val1=int(input("Enter the natural number: "))
for i in range(val1):   ##### The range should be important , otherswise you get the object error.
    natrual.append(i+1)   ##### To append and store the values into list
print(natrual)


sum=0
for i in natrual:    ######  We take the values from the list and sum the values
    sum=sum+i
print(sum)
