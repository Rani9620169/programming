'''Create an ElectricityBill class that stores a customer's name and electricity units used.
 Calculate the bill using these rates: 3 per umit for the first 100 units, 5 per unit for the next 100 units, and 7 per unit 
 for inits above 200. Add a fixed charge of 50. Display the customer's name, units used, and total bill.
 If the entered units are negative, display an error message.'''

class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        # Negative units ka check
        if self.units < 0:
            print("Error: Units cannot be negative!")
            return None
            
        bill = 0
        units = self.units
        
        # Slab 1: First 100 units @ ₹3
        if units <= 100:
            bill += units * 3
        else:
            bill += 100 * 3
            units -= 100
            
            # Slab 2: Next 100 units @ ₹5
            if units <= 100:
                bill += units * 5
            else:
                bill += 100 * 5
                units -= 100
                
                # Slab 3: Units above 200 @ ₹7
                bill += units * 7
                
        # Fixed charge add karna
        total_bill = bill + 50
        return total_bill

    def display_bill(self):
        amount = self.calculate_bill()
        if amount is not None:
            print("\n--- Electricity Bill ---")
            print(f"Customer Name : {self.name}")
            print(f"Units Used    : {self.units}")
            print(f"Total Bill    : ₹{amount}")

# Execution check
customer1 = ElectricityBill("Rahul Sharma", 250)
customer1.display_bill()

customer2 = ElectricityBill("Amit Verma", -10)
customer2.display_bill()