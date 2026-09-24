#7.write a python program to store multiple student recodrs as a list of tuples.Each tuple should contain name, roll number, and marks.Display students who sccored above 75.


students = [
    ("Aditi", 101, 85),
    ("Rahul", 102, 70),
    ("Neha", 103, 90),
    ("Riya", 104, 65)
]

print("Students scoring above 75:")

for student in students:
    if student[2] > 75:
        print(student)