#6.write a program to reverse every kth row in a matrix.

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Enter value of k: "))

for i in range(k-1, rows, k):
    matrix[i].reverse()

print("Updated Matrix:")
for row in matrix:
    print(row)