#2.take roll no. like 2024a1r057 and  axact admission year.
roll_num = "2024A1R57"

year = roll_num[:4]
program_code = roll_num[4:7]
digits = roll_num[7:]

print("Admission Year:", year)
print("Program Code:", program_code)
print("Roll Number Digits:", digits)