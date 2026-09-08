#8.write a python program to take a sentence,detect double spaces,and replace them with single spaces.
sentence = input("Enter a sentence")
while " " in sentence:
    sentence = sentence.replace(" ","_")
    print(sentence)