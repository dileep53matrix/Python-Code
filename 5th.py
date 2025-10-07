# lecture  Loops
# i = 1 
# while i <= 100:
#     print("Dileep", i)
#     i += 1
# print("end")

# while True:
#     print("Dileep")
# print("end")
# i = 1 
# while i <= 5:
#     print("hello")
#     i += 1

# i = 100 
# while i >= 1:
#     print(i)
#     i -= 1

#print the multification table of a number n

# i = 1
# while i <= 10:
#     print(i*3)

#     i += 1

# print the elements of the following list using a loop

# nums = [1,4,9,16,25,36,49,64,81,100]
# print(len(nums))
# idx = 0
# while idx < len(nums):
#     print(nums[5])
#     idx += 1
# nums = (1,4,9,16,25,36,49,64,81,100)
# x= 49
# i = 0 
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx" , i)
#     i +=1

# Break and continue 
#Break

# i = 1
# while i <= 10:
#     print(i)
#     if(i == 6):
#         break

#     i += 1


# i = 1
# while i <= 10:
#     if(i == 7):
#         i += 1
#         continue
#     print(i)

#     i += 1
    
#loops in python

# nums = (1,2,3,4,5,6,7,8,9)

# for val in nums:
#     print(val)
# else:
#         print("end")

# practice questions
# print the elements of the following list using a loop 

# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# for i, val in enumerate(nums):
#     if val == x:
#         print(i)   # prints 4

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0 
# for val in nums:
#     if(val == x):
#         print("found at i", i)
#     i += 1

#range
# print(range(5))
# seq = range(10)
# for i in seq:
# print(seq[2])
# print(seq[3])
# print(seq[4])
# print(seq[5])
# print(seq[9])
# seq = range(10, 50, 2)
# for i in seq:
#     print(i)
# seq = range(101)
# for i in seq:
#     print(i)

# seq = range(100, 0, -1)
# for i in seq:
    # print(i)

# seq = range(0,50,5)
# for i in seq:
#     print(i)

# n = int(input("enter your number:"))
# for i in range(1,11):
#     print(n*i)

# for i in range (1,20):
#     pass
# print("dileep")