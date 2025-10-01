#concatenation

# str1 = ("how are you Dileep , i am a good boy.")
# str2 = ("Dileep")
# str3 = ("learning python is a new skill for me.")
# str4 = "dileep choudhary"

# print(str1 + " " +str2 + " " + str3) 
# print(len(str1))
# print(len(str2))
# print(len(str3))
# print(len(str4))

#Indexing

# str1 = "Dileep Choudhary"
# str2 = "Matrix"

# print(str2[3])

# print(str1[5])
# print(len(str1))


#slicing
# str1 = "Dileep Choudhary"
# str2 = "Matrix"

# print(str1[2:6])

# print(str1[6:7])
# print(str1[0:6])
# print(str2[0:6])

# print(str1[0:6] + str1[6:7]+ str2[0:6])

# print(str2[2:5])

#negative index

# str1 = "Dileep Choudhary"
# str2 = "Matrix"

# print(str1[-11:-2])

# print(str2[-6:])

#string functions 

str1 = "i am a good boy . my name is Dileep Choudhary. now days i am learning python programming language ."
str2 = "Hello Dileep , You are doing great . but never stop this practice , it may be helpful in your future Dileep."

# print(str1.endswith("age ."))

# print(str2.endswith("Dileep."))

# str = str2.replace("i" , "m") 
# print(str1.capitalize())


# print(str)

# print(str1.replace("a" , "o"))

# print(str1.find("Dileep"))
# print(str2.find("i"))

# print(str1.count("Dileep"))
# print(str2.count("Dileep"))
# print(str1.count("o"))
# print(str2.count("n"))
# print(str1.count("am"))

#practice
#write a program to input user's first name and its length

# str = input("enter first name:")

# age = int(input("enter age"))
# print("length of name", len(str))
# print(type(age))


#write a program to find occurrence of $ in a string

# str = "i am$ and what are $ you. $ yes good $."

# print(str.count("$"))

# conditional staements 

# num = 95

# if(num >= 90):
#     print("grade A, Shabash beta")  
# elif(num >= 75 and num < 90):
#     print("grade B , ok beta")
# else:
#      print("grade C, practice can be improve your marks")


#let's practice 
# WAP to check if a number entered by the user is odd or even

# num = int(input("enter number:"))


# if(num%2==0):
#     print("even")
# else:
#     print("odd")

# WAP to find the greatest of 3 numbers entered by user

# num1 = int(input("first number:"))
# num2 = int(input("second number:"))
# num3 = int(input("third number:"))

# if(num1>num2):
#     print("num1 is greatest number")
# elif(num2> num3, num2>num1):
#     print("num2 is greatest number")
# else:
#     print("num1 is greatest number")

# WAP to check if a number is a multiple of 12 or not.

num = int(input("enter number:"))

rem = num%12

if( rem == 0):
    print("yes ,it is multiple of 12")
else:
    print("no, it is not multiple of 12")