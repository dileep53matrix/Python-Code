#Dictionary & Set in Python
#Dictionary in Python 

# dict = {
# "name" : "Dileep",
#  "cgpa" : 8.03,
#   "marks" : [77 ,85, 92]
# }

# dict["Dileep"] = "be good"
# print(dict)
# print(dict["name"])

# print(dict["cgpa"])
# print(dict["marks"])
# print(dict["Dileep"])

#nested dictionary

# student = {
#   "name" : "Dileep",
# "score" : {
#   "chem" : 77,
#   "math" : 85,
#   "phy" : 92
# }
# }

# print(student["name"])
# print(student["score"])
# print(student["score"]["phy"])
# print(student["score"]["chem"])

# print(len(list(student.keys())))
# print(len(list(dict.keys())))
# print(list(dict.keys()))
# print(list(student.keys()))

# print(list(student.values()))
# print(list(student.items()))
# print(list(student.get("score")))
# new_dict = {"name" : "Matrix", "age" : 19}
# print(student.get("score"))
# print(student.update(new_dict))
# print(student)

#set in python 

# Set is the collection of the unordered items.
# Each elements in the set must be unique & immutuable

# set = {1,2,3,4,5}
# set2 = {1,2,2,2,5}
# set.add(6)
# print(set.add(6))
# print(set.remove(2))
# print(set.clear())
# print(set.pop())
# print(set.union(set2)) # combines both set values & returns new 
# print(set.intersection(set2)) #combines common values and returns new

# print(set)

#let's practice 

# dict = { 
# "cat" : "a small animal",
# "table" : ["a piece of furniture", "list of facts and figures"]
# }

# print(dict)

# sub = {"python","python","python","c++","java", "c++", "java", "javascript", "c"}
# print(len(sub))
# print(sub)

# marks ={} #dict

# x = int(input("enter maths marks :"))
# marks.update({"maths" : x})

# x = int(input("enter phy marks :"))
# marks.update({"phy" : x})

# x = int(input("enter chem marks :"))
# marks.update({"chem" : x})


# print(marks)

# values = {9,"9.0"}

# print(values)

values = {
("float", 9.0),
("int" , 9)
}

print(values)