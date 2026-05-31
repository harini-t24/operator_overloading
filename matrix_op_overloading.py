class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __add__(self, other):
        result = []

        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)
    def __sub__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)
    def __mul__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                total = 0
                for k in range(len(other.matrix)):
                    total += self.matrix[i][k] * other.matrix[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)
    def __str__(self):
        return str(self.matrix)
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))
if c1 != r2:
    print("Invalid Input")
    print("Matrix multiplication not possible")
else:
    print("Enter elements of first matrix:")
    m1 = []
    for i in range(r1):
        row = list(map(int, input().split()))
        m1.append(row)
    print("Enter elements of second matrix:")
    m2 = []
    for i in range(r2):
        row = list(map(int, input().split()))
        m2.append(row)
    matrix1 = Matrix(m1)
    matrix2 = Matrix(m2)
    if r1 == r2 and c1 == c2:
        print("Addition:")
        print(matrix1 + matrix2)
        print("Subtraction:")
        print(matrix1 - matrix2)
    else:
        print("Addition and Subtraction not possible")
    print("Multiplication:")
    print(matrix1 * matrix2)
