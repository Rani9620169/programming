'''Write a python program'''

import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:

    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Right-angled triangle")
    else:
        print("Not a right-angled triangle")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Area =", area)

else:
    print("Invalid triangle")