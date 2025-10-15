#functions in python

# def calc_sum(a , b):
#     sum = a + b 
#     print(sum)
#     return sum

# calc_sum( 5,22)


# calc_sum(4, 45)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()

# def calc_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(5, 85,185)

cities = ["Delhi", "pune" , "jaipur", "tonk"]
heroes = [ "batman", "superman","spiderman" ," thor" , "hulk" ]

# print(heroes[0], end=" ")
# print(heroes[3] , end=" ")
# print(heroes[2])

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)
    
# print_len(cities)
# print_len(heroes)


# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i   # multiply fact by i in each step
# print(fact)

# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)
# calc_fact(7)
# calc_fact(6)

# def converter(usd_val):
#     inr_val = usd_val*89
#     print(usd_val , "Usd=", inr_val, "Inr")

# converter(1000000)

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(6)

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1

#     return fact(n-1)*n

# print(fact(2))

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(6)
# print(sum)
# def calc_sum(n):
#     if n == 0:
#         return 0
#     return calc_sum(n-1) + n   # add n, not 1

# total = calc_sum(6)
# print(total)

def print_list( list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx +1)

cities = ["tonk", "jaipur", "Bangalore"]
print_list(cities)
