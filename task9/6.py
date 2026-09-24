#6.write a python program to store one student data as a tuple: name ,roll,and marks.Display grade based on marks.

student = ("Aditi", 101, 85)

print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])

marks = student[2]

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)