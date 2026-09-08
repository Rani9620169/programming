#5.take password
password = input("Enter a password:")

length_ok = len(password) >=8

has_at = "@" in password

different_ends = password[0] != password[-1]

print("Is length valid (>=8)?:", length_ok)
print("Contains '@'?:", has_at)
print("First and last characters different?:", different_ends)