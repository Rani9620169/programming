#9.write a python program to input two lists and create a third list containing common elements.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

list3 = []

for n in list1:
    if n in list2 and n not in list3:
        list3.append(n)

print("Third list:", list3)