#3.wrte a python program to input a list of numbers in alist and find the second largest number.

numbers = list(map(int, input("Enter numbers: ").split()))

numbers = list(set(numbers))
numbers.sort()

print("Second largest:", numbers[-2])