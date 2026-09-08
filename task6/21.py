#4.write a python program to create a simple password validation system.

while True:
    password = input("Enter a password: ")
    
    
    if len(password) >= 8 and "@" in password:
        print("Password accepted.")
        break  
    else:
        print("Weak password. Try again.")