#1.write a python to dertermine whether a student is eligible for a scholarship.The scholarship should be granted if the student satisfies either of the following conditions (a)The student has a CGPA of 8.5 or above and attendence of 85 percent or above.(b)The student has won a national competition.The program should take CGPA , attendence percentage.

cgpa = float(input("Enter student's CGPA: "))
attendance = float(input("Enter attendance percentage: "))
won_competition = input("Has the student won a national-level competition? (yes/no): ").strip().lower()

condition_a = (cgpa >= 8.5) and (attendance >= 85)
condition_b = (won_competition == "yes")

if condition_a or condition_b:
    print("The student is eligible for the scholarship!")
else:
    print("The student is not eligible for the scholarship.")
