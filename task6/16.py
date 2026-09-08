#4.take name ,branch and year.
name = input("Enter name: ")
branch = input("Enter branch: ")
year = input("Enter year: ")

codename = (name[:2] + branch[-2:] + year) * 2
print("Generated Code Name:", codename)