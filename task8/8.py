#8.write a python program to count how many times a particular element appears in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

x = int(input("Enter element to search: "))

print("Occurrences:", numbers.count(x))