#4.write a puthon program to input a list of numbers and create a new list containing only unique elements.

numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print("Unique list:", unique)