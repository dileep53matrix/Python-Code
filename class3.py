# Program to read 6 subject marks and display them from highest to lowest using Bubble Sort 

marks = []
# 6 subject marks
for i in range(6):
    mark = int(input(f" Enter the mark{i+1}:"))
    marks.append(mark)
#length
n = len(marks)
print(len(marks))
# for listing highest tp lowest
for i in range(n-1):
    for j in range(0 , n-i-1):
        if marks[j]< marks[j+1]:
            # swap the elements
            marks[j], marks[j+1] = marks[j+1], marks[j]

#display the marks
print("\n Marks highest to lowest :")
for mark in marks:

    print(mark)
