# #read two numbers from the keyboards

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))

# #display menu
# print("\n Select the operation to perform:")
# print("1.Addition")
# print("2.sub")
# print("3.mul")
# print("4.divide")

# #user choice 
# choice = int(input("enter your choice :"))

# if choice == 1:
#     result = num1 + num2
#     print("addition:", result)

# elif choice == 2:
#     result = num1-num2
#     print("Subt:", result)

# elif choice == 3:
#     result = num1*num2
#     print("Mul:", result)
    
# elif choice == 4:
#     result = num1/num2
#     print("Devide:", result)

# else:
# #     print( "Dileep")

# #read the name and year ofbirth 
# name = input("enter name:")
# birth_year = int(input("enter birth year:"))

# current_year = 2025 
# age = current_year-birth_year

# print("\nName:", name)
# print("Age :",age)

# if age >=60:
#     print("I am a senior citizen ")

# else:
#     print("I am not senior citizen")

# dap to generate fibonacci sequence

N = int(input("enter the number of terms (N):"))

#check for valid input 
if N < 0:
    print("write positive number")

else:
    fibonacci = [0,1] #starting values 
    if N == 1:
        print("Fibonacci sequence:", [0])

    elif N == 2:
        print("Fibonacci sequence:", fibonacci)

    else:
        for i in range(2 , N):
            next_term = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(next_term)
        print("Fibonacci sequence:", fibonacci)


#WAP create list 
list =[1,2,6]

# el = input("enter the element:")
# position = int(input("enter the position:"))

# list.insert(position, el)
# print(list)
# if el in list:
#     list.remove(el)
#     print(list)

# else:
#     print("not in list")

# list.append(el)
len(list)