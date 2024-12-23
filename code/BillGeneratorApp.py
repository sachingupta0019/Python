# Bill Generator APP

No_of_Products = int(input("Enter Number of Products: "))
products = []
total_bill = 0

for product in range(1,No_of_Products+1):
    name = input("Product Name: ")
    quantity = float(input("Quantity: "))
    price = float(input("Price: "))
    products.append((name, quantity, price))

print("Welcome to Om Shopping cart")
for item in products:
    total = item[1] * item[2]
    print(f"Item : {item[0]} \nQuantity : {item[1] : 3.2f} \nPrice : {item[2] : 6.2f} \nTotal : {total : 7.2f} ")
    total_bill = total_bill + total
print(f"Total Bill : {total_bill : 7.2f}")
print("Thank you for Shopping!")