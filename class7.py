students ={}
n = int(input("enter number of students:"))
for i in range(n):
    name = input("enter student name:")
    marks = int(input("enter marks:"))
    students[name] = marks
total  = sum(students.values())
average = total/n 
topper = max(students, key = students.get)
print("\n...students Report...")
print("average Marks:", average)
print("Topper:",topper, "with", students[topper],"marks")