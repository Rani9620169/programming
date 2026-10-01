'''Create a database using list and tuples. Each student record must contain roll number,
 name, branch, and CGPA. Store each record as a tuple inside a list. 
 Display all records and seacrh for a student using roll number. 
 Condition:
 -Each record should be stored as a tuple.
 -The complete database should be stored as a list.
 -Roll numbers must be unique.'''

database = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Roll Number: "))

    exists = False
    for rec in database:
        if rec[0] == roll:
            exists = True

    if exists:
        print("Roll number already exists!")
        continue

    name = input("Name: ")
    branch = input("Branch: ")
    cgpa = float(input("CGPA: "))

    student = (roll, name, branch, cgpa)
    database.append(student)

print("\nAll Records:")
for rec in database:
    print(rec)

search = int(input("\nEnter roll number to search: "))

for rec in database:
    if rec[0] == search:
        print("Record Found:")
        print(rec)
        break
else:
    print("Record not found")