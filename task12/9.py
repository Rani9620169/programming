'''Write a python program that creates a parkingTicket class for calculating the parking fee for one vehicle.
The program must:
1.Ask the user to enter the vehicle number and parking duration in hours.The duration may include a fraction, such as 2.5 hours.
2.Calculate the fee using the billable hours:
  -Each started hour counts as one full hour. For example, 2.1 hours is billed as 3 hours.
  - change 30 per billable hour for the first two hours.
3.Display the vehicle number, actual parking duration, and total fee.
4.If the duration is zero or negative, display an error message and do not calculate a fee.
Example: A vehicle parked for 2.5 hours is billed for 3 hours. The fee is 30+ 30 + 20 = 80.'''

import math

class ParkingTicket:
    def __init__(self):
        self.vehicle_number = ""
        self.duration = 0.0
        self.billable_hours = 0
        self.total_fee = 0.0

    def process_ticket(self):
        
        self.vehicle_number = input("Enter the vehicle number: ")
        
        try:
            self.duration = float(input("Enter parking duration in hours (e.g., 2.5): "))
        except ValueError:
            print("Error: Please enter a valid numerical value for duration.")
            return

        
        if self.duration <= 0:
            print("Error: Duration must be greater than zero. Fee cannot be calculated.")
            return

        
        self.billable_hours = math.ceil(self.duration)
        
        

        if self.billable_hours <= 2:
            self.total_fee = self.billable_hours * 30
        else:
            self.total_fee = (2 * 30) + ((self.billable_hours - 2) * 20)

        
        print("\n--- Parking Ticket Summary ---")
        print(f"Vehicle Number:         {self.vehicle_number}")
        print(f"Actual Parking Duration: {self.duration} hours")
        print(f"Billable Hours:         {self.billable_hours} hour(s)")
        print(f"Total Fee:              ₹{self.total_fee}")

if __name__ == "__main__":
    ticket = ParkingTicket()
    ticket.process_ticket()