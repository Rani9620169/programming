'''Create a product class with the product name, price, and quantity.Add an instance method to calculate the total cost. 
Tkae these values from the user and display the product name and total cost.'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    
    def calculate_total_cost(self):
        return self.price * self.quantity


prod_name = input("Enter product name: ")
prod_price = float(input("Enter product price: "))
prod_qty = int(input("Enter product quantity: "))

prod = Product(prod_name, prod_price, prod_qty)
print(f"\nProduct Name: {prod.name}")
print(f"Total Cost: ${prod.calculate_total_cost():.2f}")