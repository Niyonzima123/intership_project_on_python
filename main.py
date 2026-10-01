class Item():
    pay_rate =0.2
    def __init__(self,name,price, quantity):
        self.name = input("enter your names")
        self.price =price
        self.quantity =quantity
    def calculate_price(self):
        return self.price *self.quantity

item1 = Item("Phone",1000,3)


print(item1.name)
print(item1.price)
print(item1.quantity)

print(item1.calculate_price())


with open('items.txt', 'w') as file:
    file.write('Alice - Score: 89 %\n')
    file.write('bob - Scole:72\n')
    




