#1.take student full name and roll no.Generated using first 3 letters of first name, first 3 letters pf last name.
full_name = ("Enter full name: ")
roll_number = ("Enter roll number: ")

space_index = full_name.find(" ")

first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

email = first_name[:3] + last_name[:3] + roll_number[-3:]

print(email)

