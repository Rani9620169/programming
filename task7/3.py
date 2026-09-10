#3.write a program to input two number and find their greatest common divisor using a loop.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


smaller = min(num1, num2)
gcd = 1

for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

print(f"The Greatest Common Divisor is: {gcd}")