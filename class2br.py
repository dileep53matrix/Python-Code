name = input("enter name:")
birth_year = int(input("enter birth year:"))

# write current year 
current_year = 2025
age = current_year-birth_year
print("\nName:",name)
print("Age", age)

if age >= 60:
    print("senior citizen")

else:
    print("not senior citizen")