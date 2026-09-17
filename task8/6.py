#6.write a python program to rotate a list one position to the right.

numbers = list(map(int, input("Enter numbers: ").split()))

numbers = [numbers[-1]] + numbers[:-1]

print("Rotated list:", numbers)