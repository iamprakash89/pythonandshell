#create a base class called shape with method area() that return 0. create a derived class called rectangle.
# and overrieds the area() method to calculate te area of rectangle.

class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()

