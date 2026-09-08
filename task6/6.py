#5.write a python program to take a word and count the number of vowels a,e,i,o,u.
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in word if char in vowels)

print(f"Number of vowels: {count}")