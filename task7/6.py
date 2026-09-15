#6.write a python program to input a decimal number and convet it into binary without using the built

n = int(input("Enter a decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    print("Binary =", binary)