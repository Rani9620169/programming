#12.write a puthon program to take a password and check whether it contains @ and has at least character.
password = input("Enter a password: ")

if "@" in password and len(password) >= 8:
    print("Valid password.")
else:
    print("Invalid password. Must contain '@' and be at least 8 character long.")