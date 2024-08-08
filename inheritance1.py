#### multi level inheritance

class grandp():
    def phone(self):
        print("Grandpa Phone")

class dad(grandp):
    def money(self):
        print("dads Money")

class son(dad):
    def laptop(self):
        print("Sons laptop")

ram=son()
ram.laptop()
ram.money()

d1=dad()
d1.phone()

ram.phone()