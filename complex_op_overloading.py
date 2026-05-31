class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return Complex(r,i)
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return Complex(r,i)
    def display(self):
        print(self.real, "+", self.imaginary, "i")
r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part of first complex number: "))
r2 = int(input("Enter real part of second complex number: "))
i2 = int(input("Enter imaginary part of second complex number: "))
c1 = Complex(r1, i1)
c2 = Complex(r2, i2)
c3 = c1+c2
c4 = c1-c2
print("\nFirst Complex Number:")
c1.display()
print("Second Complex Number:")
c2.display()
print("Sum of Complex Numbers:")
c3.display()
print("Subtraction of Complex Numbers:")
c4.display()
