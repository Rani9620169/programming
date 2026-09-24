#3.write a python program to show that tuple values cannot be changed directly. Conert tuple into list, update it, and convert it back into tuple.

t = (10, 20, 30)

print("Original tuple:", t)

lst = list(t)
lst[1] = 50

t = tuple(lst)

print("Updated tuple:", t)