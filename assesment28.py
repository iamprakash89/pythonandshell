class laptop():
    price=""
    processor=""
    ram=""

HP=laptop()
DELL=laptop()
LENOVO=laptop()

HP.price="10000"
HP.processor="1GHZ"
HP.ram="16GB"

DELL.price="11000"
DELL.processor="2GHZ"
DELL.ram="32GB"

LENOVO.price="12000"
LENOVO.processor="3GHZ"
LENOVO.ram="64GB"

print(DELL.ram," ",DELL.processor," ",DELL.price)
print(HP.ram," ",HP.processor," ",HP.price)
print(LENOVO.ram," ",LENOVO.processor," ",LENOVO.price)