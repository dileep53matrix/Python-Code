#DAP for mathemetics calculations
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

#choose action 
print("\n Select the operation to perform")
print("1.Addition")
print("2.Subtraction")
print("3.Multification")
print("4.Division")

#your choice
choice = int(input("enter choice between 1 to 4 :"))

# conditions according opreations
if choice == 1:
    result = num1 + num2
    print("Addition:", result)

elif choice==2:
    result = num1 - num2 
    print("Sub:",result)

elif choice ==3:
    result = num1*num2
    print("Multificatiom:", result)

elif choice == 4:
    result = num1/num2
    print("Division:", result)

else:
    print("error")