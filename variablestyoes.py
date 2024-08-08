class phone():
    def __init__(self,brand,price,ctype):
        self.brand=brand
        self.price=price
        self.ctype=ctype
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("ctype: ",self.ctype)

samsung=phone("samsung","10000","B-type")
samsung.display()