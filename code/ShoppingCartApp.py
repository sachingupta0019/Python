#################################################
##############  Shopping Cart App  ##############
#################################################

class CartApp:
    def __init__(self):
       self.items = {}

    def add_product(self, item, quantity):
        self.items[item] = quantity

    def remove_product(self, item):
        self.items.pop(item)

    def change_quantity(self, item, quantity):
        self.items[item] = self.items[item] + quantity

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        str = "Cart Conatins : "
        for item in self.items:
            str += f"{item} = {self.items[item]}"
            return str
        
customer1 = CartApp()
customer1.add_product("laptop", 5)
print(customer1)