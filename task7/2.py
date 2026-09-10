#2.write a python program to input a number and check whether it is prime or not.A number is prime if it has no divisor other than 1 and itself.


num = int(input("Enter a number to check: "))


if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  
            break             
            
    if is_prime:
        print("It is a prime number")
    else:
        print("Not a prime number")