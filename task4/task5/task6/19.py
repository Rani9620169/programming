
CORRECT_PIN = "1234"


while True:
    user_pin = input("Enter your 4-digit PIN: ")
    

    if len(user_pin) != 4 or not user_pin.isdigit():
        print("Error: The PIN must contain exactly 4 digits! Please try again.\n")
        continue  # Skips the rest of the loop and starts over
        
    
    if user_pin == CORRECT_PIN:
        print("Success! The lock is open. Welcome!")
        break  # Stops the loop completely because we are done
    else:
        print("Incorrect PIN. Please try again.\n")