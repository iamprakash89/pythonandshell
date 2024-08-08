class goa:
    drink=""
    name=""
    def party(self):
        print("SURESH Lets Party.....")
    def beach(self):
        print("RAMESH Lets enjoy beach....")

ramesh = goa()
suresh = goa()

suresh.drink="yes"
ramesh.drink="No"
suresh.name="suresh"
ramesh.name="ramesh"

print("drink:",ramesh.drink)
print(ramesh.name)
ramesh.beach()

print("drink: ",suresh.drink)
print(suresh.name)
suresh.party()
