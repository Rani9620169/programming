#5.write a python program to input marks of 5 students.

for i in range(1, 6):
    marks = float(input(f"Enter marks for student {i}: "))
    
    
    if 0 <= marks <= 100:
        print(f"Valid marks: {marks}")
    else:
        print("Invalid marks skipped")