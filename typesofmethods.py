## methods are nothing but function

class laptop():
    ctype="C TYPE"
    def __init__(self):
        self.brand=""
        self.price=43

    def setprice(self,price):
        self.price=price

    def getrpice(self):
        print(self.price)

hp=laptop()
#hp.setprice(2000)
hp.getrpice()