#### count the number which are divisible by 3 and 5 Range(1-100)
count=0
for i in range(1,101):
    if (i%3==0 and i%5==0):
        count=count+1
print("the total count of divisible by 3 and 5 are: ",count)
