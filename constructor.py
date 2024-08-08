class laptop():
    def __init__(self):   #### it is a default construction, So you dont need to call the function
        print("constructor calling")
    def display(self):   #### This is not default constructor, you have to call when you need
        print("display function")

HP=laptop()
HP.display()