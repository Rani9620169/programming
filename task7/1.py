#1.write a python program that makes ask the user to enter a username and password.The user should get only 3 letters.


correct_username = "student"
correct_password = "coding123"


for attempt in range(3):
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")
    
    
    if user_input == correct_username and pass_input == correct_password:
        print("Login Successful")
        
else:
    
    print("Account Locked")