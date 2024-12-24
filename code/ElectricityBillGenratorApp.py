# Electricity Bill Generator APP : 

# ******         varibales    *******
# customer_id
# name
# units

# *********      Constraints    ********
# First 100 units : Rs 5/unit
# Next 100 units  : Rs 7/unit
# Next all units  : Rs 9/unit

class ElectricityBill:
    def __init__(self,customer_id, name, units):
        self.customer_id = customer_id
        self.name = name
        self.units = units
    

    print("************ Welcome to Power Grid *******************\n")
    def calculate_bill(self):
        bill = 0
        if self.units > 100:
            bill += (5*100)
            print(f"Bill for First 100 Units : {bill}")
        else:
            bill += 5 * self.units
            print(f"Bill for {self.units} Units is : {bill}")

        if self.units > 200:
            bill_temp = (7*100)
            bill += bill_temp
            print(f"Bill for Next 100 units  : {7*100}")
        elif self.units > 100 and self.units <= 200:
            bill_temp = 7 * (self.units - 100)
            bill += bill_temp
            print(f"Bill for {self.units - 100} Units is {bill_temp}")
        
        if self.units > 200:
            bill_temp = 9*(self.units - 200)
            bill += bill_temp
            print("Bill for above 200 units :",bill_temp)

        print("\n")
        print("**************************************")
        print(f"\tFinal Bill is : {bill}")
        print("**************************************")
        print("\t Thank you !...")


sachin = ElectricityBill(81818990,"Rocky", 129).calculate_bill()