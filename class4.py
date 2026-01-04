class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def add(self,other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def display(self):
        print(f"{self.real} + {self.imag}:")
        
n = int(input("enter number of complex(>=2):"))
numbers = []
for i in range(n):
    r = float(input(f"enter real part of complex"))
    img = float(input(f"enter real part of complex"))
    numbers.append(Complex(r,img))
result = numbers[0]
for i in range(1, n):
    result = result.add(numbers[i])
    print("\n final sum is")
    result.display()
    