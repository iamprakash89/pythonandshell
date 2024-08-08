## Multiple Inheritance

class dad():
    def money(self):
        print("dad money")

class land():
    def importance(self):
        print("Important land")

class son2(dad,land):
    pass
class son3(dad):
    pass

s2=son2()
s2.money()