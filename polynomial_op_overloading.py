class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result)
    def __str__(self):
        return str(self.coeffs)
p1 = list(map(int, input("Enter first polynomial coefficients: ").split()))
p2 = list(map(int, input("Enter second polynomial coefficients: ").split()))
poly1 = Polynomial(p1)
poly2 = Polynomial(p2)
result = poly1 * poly2
print("First Polynomial:", poly1)
print("Second Polynomial:", poly2)
print("Multiplication Result:", result)
