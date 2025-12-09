N = int(input("enter the number:"))
#check for valid input
if N<=0:
    print("please enter positive number")

else:
    fibonacci = [0,1]
    if N ==1:
        print("Fibonacci Seq", [0])

    elif N == 2:
        print("Fibonacci seq",fibonacci)

    else:
        for i in range(1,N):
            next_term = fibonacci[i-1]+fibonacci[i-2]
            fibonacci.append(next_term)

    print("Fibonacci seq ", fibonacci)