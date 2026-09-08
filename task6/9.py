#9.write a python program to take a word and print it in reverse order using slicing.Also check whether it is the same forword and backword.
word = input("Enter a word: ")
reversed_word = word[: :-1]

print(f"Reversed word: {reversed_word}")

if word.lower() == reversed_word.lower():
    print("The word is the same forward and backword.")
else:
    print("The word is not the same forward and backword.")