#### inheritance and Types
## it is nothing but one class access a another class, that is called a nheritance
#### This is called single inheritance


class dad():
    def phone(self):
        print("dads phone")

class mom(dad):   #### single Inheritance
    def sweet(self):
        print("mom has sweet")

class son(dad,mom):      #### Multiple Inheritance  
    def laptop(self):
        print("sons laptop")

ram=son()
ram.phone()
ram.sweet()


