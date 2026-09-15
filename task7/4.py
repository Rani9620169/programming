#4.write a python program to check whether a number is a perfect number.A number is perfect if the sum of its proper divisiors is equal to the number itself.

n = int(input("Enter a number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total = total + i

if total == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")