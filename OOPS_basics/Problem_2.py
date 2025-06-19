#Create a class calculator which can find square, cube, square root of a number

class calculator:
    def __init__(self,number):
        self.number=number
    @staticmethod
    def greet():
        print("Hello!!!")
    def square(self):
        formula = self.number*self.number
        print(f"Square of a {self.number} is {formula}")
    def cube(self):
        third = self.number*self.number*self.number
        print(f"Cube of a {self.number} is {third}")
    def square_root(self):
        root = self.number**1/2
        print(f"Square root of {self.number} is {root}")

num1 = calculator(4)
num1.greet()
num1.square()
num1.cube()
num1.square_root()

    

