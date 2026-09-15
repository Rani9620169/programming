#8.write a python program to repeatdly calculate the sum of digits of a numbers until the result becomes a single didgit.

n = int(input("Enter a number: "))

while n >= 10:
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    n = total

print("Single digit =", n)