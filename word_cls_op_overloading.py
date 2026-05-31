class Word:
    def __init__(self, text):
        self.text = text
    def __add__(self, other):
        return Word(self.text + other.text)
    def __eq__(self, other):
        return self.text == other.text
w1 = input("Enter first string: ")
w2 = input("Enter second string: ")
obj1 = Word(w1)
obj2 = Word(w2)
result = obj1 + obj2
print("\nConcatenated String:", result.text)

if obj1 == obj2:
    print("Both strings are equal")
else:
    print("Both strings are not equal")
