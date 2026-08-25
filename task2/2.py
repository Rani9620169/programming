#write a python program to calculate simple interested and total amount using principal, rate ,and time entered by the user.

p = int(input())
r = int(input())
t = int(input())
si = (p*r*t)/100
amount = p+si
print(si)
print(amount)
