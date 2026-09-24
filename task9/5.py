#5.write a python program to check whether a given value is present in a tuple.If present , display its position.

t = (10, 20, 30, 40, 50)

n = int(input("Enter value: "))

if n in t:
    print("Position =", t.index(n))
else:
    print("Value not found")