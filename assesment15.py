#### print the count of odd number

print("print the count of odd number and even number between 1 to 10")

odd=0
even=0
for i in range(1,11):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("the count of even number: ",even)
print("The count of odd number: ", odd)