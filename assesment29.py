### create a clss called Animal with a methos sound() that prints "Animal makes sound". 
# create a derived class called Dog that inherits from Animal and overrides the sound() method to print "Dog Barks"
## Create another derived class called Bird that inherits from Animal and overrides the sound() method to print "Bird Sing"

class Animal():
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Bird Sing")


b1=Dog()
b1.sound()