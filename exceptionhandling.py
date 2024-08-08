#compile time error

print("hello")
print("hai")
#printtt("compileerritesting")   #### compilation error

#logical error
a=10
b=20
print(a+a)  ## the program needs to be add a and b.

## runtime error
try:
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    print(a+b)
#except Exception:
 #   print("Enter he correct value")
except Exception as e:
    print("enter the correct value",e)
finally:
    print("end of the script")