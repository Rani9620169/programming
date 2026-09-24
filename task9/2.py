#2.write a python program to store all month names in a tuple.Input a month number and display the corresponding month name.


months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

n = int(input("Enter month number: "))

print("Month =", months[n-1])