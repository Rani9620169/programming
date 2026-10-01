'''1.write a python program to input a students marks in n consecutive and store them 
 in a list . Find the longest consecutive sequence in which each marks is strickly 
 greater than the previous marks.    Display the sequence, its length , and its
 starting and ending test numbers as a tuple.If multiple sequence have the same
 maximum length, display the first one.  marks:[55, 60, 68, 62, 65, 70, 78, 74]  
longest improving sequence:[62, 65, 70, 78]  numbers of tests:4  test range:(4,7)'''


n = int(input("Enter number of tests: "))

marks = []
for i in range(n):
    marks.append(int(input(f"Enter marks for test {i+1}: ")))

longest = []
current = [marks[0]]

start = 1
best_start = 1
best_end = 1

for i in range(1, n):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        if len(current) > len(longest):
            longest = current.copy()
            best_end = i
            best_start = i - len(current) + 1
        current = [marks[i]]

# Check the last sequence
if len(current) > len(longest):
    longest = current.copy()
    best_start = n - len(current) + 1
    best_end = n

result = (longest, len(longest), best_start, best_end)

print("Longest improving sequence:", longest)
print("Number of tests:", len(longest))
print("Test range:", (best_start, best_end))






