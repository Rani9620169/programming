#14.write a python program to print a centered pyramid using stars.

n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)