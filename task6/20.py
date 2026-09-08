#3.write a puthon program to calculate the final bill ammount after discount.

bill_amount = float(input("Enter the total bill amount: "))

if bill_amount > 5000:
    discount_percent = 20
elif bill_amount >= 3000:
    discount_percent = 10
else:
    discount_percent = 0


discount_amount = (discount_percent / 100) * bill_amount

final_bill = bill_amount - discount_amount

print("Discount Amount:", discount_amount)
print("Final Bill Amount Payable:", final_bill)