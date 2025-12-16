# WAP for create a list
list = [1,5]
# for adding an element 
el = int(input("enter the element"))
# for place on the position
position = int(input("enter the position number:"))

list.insert(position , el)

print("after insert the el the list:", list)
# for remove the el 
if el in list:
    list.remove(el)
    print("list after removing el", list)
else:
    print("the el not i list")
  
  
