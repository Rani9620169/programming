#10.write a python program to take first name and last name and print initials.
first_name = ("Enter a first name: ")
last_name = ("Enter a last name: ")

initials = f"{first_name[0].upper()}.{last_name[0].upper()}."

print(f"Initials: {initials}")