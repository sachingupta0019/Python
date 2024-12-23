# Cafe management System
print("Welcome to Om Cafe\n")
menu = {
    'coffee' : 30,
    'lemonade': 70,
    'dosa' : 120,
    'idli' : 80,
    'poha' : 60,
    'uttapam' : 85,
}
bill = 0
bill_detail = {}
for items in menu:
    print(items.ljust(10),"-", menu[items])

while True:
    order = input("Please order the Items or enter Done to proceed.:\n").lower()
    if order == "done":
        break
    elif order in menu: 
        quantity = int(input("Quantity: "))
        bill_detail[order] = quantity
        total = menu[order] * quantity
        bill = bill + total
    else:
        print("Item not found.")

print("Item Quantity  Total")
for item in bill_detail:
    item_cost = (bill_detail[item] * menu[item])
    total_bill = bill + item_cost
    print(f"{item.ljust(5)}\t {bill_detail[item]}\t {item_cost}")
print(f"Bill is {bill} ")
print(f"Bill with GST {bill+(18/100)*bill}")
print("Thank you for visiting.")