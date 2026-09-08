#7.write a python program to detect whether a comment is spam or not.A comment should be treated as spam if it contains of these kaywords:"make a lot of money",


comment = input("Enter a comment: ")


keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

is_spam = False


for phrase in keywords:
    if phrase in comment:
        is_spam = True
        break


if is_spam:
    print("This comment is spam.")
else:
    print("This comment is safe.")