def max_of_three(a, b, c):
    return max(a, b, c)

def armstrong(n):
    digits = str(n)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == n

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest =", max_of_three(x, y, z))

num = int(input("Enter a number: "))

if armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")