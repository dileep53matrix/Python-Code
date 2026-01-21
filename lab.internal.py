# students= {}
# n = int(input("enter students Number:"))
# for i in range(n):
#     name = input("enter students name")
#     marks = int(input("enter the marks"))
#     students[name] = marks
    
# total = sum(students.values())
# average = total/n

# topper = max(students, key = students.get)

# print("Average:", average )
# print("Topper:", topper ,"with", students[topper] , marks)


# import csv 
# values = []
# with open("data.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         values.append(float(row["temp"]))
        
# print("Max:", max(values))
# print("Min:", min(values))
# print("average :", sum(values)/len(values))



# import csv 
# values = []

# with open("data.csv") as f:
#     reader = csv.DictReader(f) 
#     for row in reader:
#         values.append(float(row["temp"]))
        
# print("max:", max(values))   
# print("min:", min(values))
# print("average:", sum(values)/len(values))





import re
paragraph = input("enter a paragraph:")
text = paragraph.lower()
words = re.findall(r"[a-zA-Z0-9']+", text )
frequency = {}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word] =1
        
longest_word = ""
for word in words:
    if len(word)> len(longest_word):
        longest_word =word
        
sentences = re.split(r"[.!?]+",paragraph)
sentences = [s for s in sentences if s.strip()]

print("total words:", len(words))
print("longest :", longest_word)
print("number of sentences ", len(sentences))
print("word frequency:")
for word , count in frequency.items():
    print(f" {word}: {count}")