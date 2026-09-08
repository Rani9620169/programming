#3.write a python program to take an email address and print the domain name.
email = input("Enter an email address: ")

domain = email.split('@')[1]
print("Domain name:", domain)