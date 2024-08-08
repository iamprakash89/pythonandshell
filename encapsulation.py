#### private variable a class ku ulla irunthu than access panna mudiyum.
### it is called encapsulation

class company():
    def __init__(self):
        self.__companyname="google"

    def companyname(self):
        print(self.__companyname)

c1=company()
c1.companyname()