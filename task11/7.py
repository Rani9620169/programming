'''7.write a python program to create records of n students.
 Store each student record as a dictionary containing roll number, name, bramch, and marks.
 Store all records in a list and seacrh for a student using roll number. 
 (Condition: Roll numbers must be umique.)'''

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Roll Number: "))

    # Check uniqueness
    exists = False
    for s in students:
        if s["roll"] == roll:
            exists = True

    if exists:
        print("Roll number already exists!")
        continue

    name = input("Name: ")
    branch = input("Branch: ")
    marks = float(input("Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

print("\nAll Records:")
for s in students:
    print(s)

search = int(input("\nEnter roll number to search: "))

for s in students:
    if s["roll"] == search:
        print("Record Found:")
        print(s)
        break
else:
    print("Record not found")