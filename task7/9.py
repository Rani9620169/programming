#1.write a puthon program to print the following patterns for n rows.

n = int(input("Enter number of rows"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")