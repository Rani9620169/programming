'''Write a program to create a simple calculator using a switch case and function for every operation.'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Result:", add(a, b))
    case 2:
        print("Result:", subtract(a, b))
    case 3:
        print("Result:", multiply(a, b))
    case 4:
        if b != 0:
            print("Result:", divide(a, b))
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid choice")