#5.write a python program to input numbers in a list create two separate lists for even and odd numbers.


numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)