'''create a class and object: student details
Problem:create a student class to store a student's name and roll number. Create an object and display the details 
using an a
instance method.'''

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")


student1 = Student("Rani Devi", 101)
student1.display_details()