#6.write a python program to input four numbers from the user and find the greatest number among them.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
greatest = num1


if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4

print("The greatest number is:", greatest)