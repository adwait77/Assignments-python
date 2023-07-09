import math

class MyMathModule:
    def __init__(self, num): 
        self.num = num

    def square(self):
        return self.num**2

    def floor(self):
        return math.floor(self.num)

    def ceil(self):
        return math.ceil(self.num)

    def logarithm(self):
        return math.log(self.num)

    def factorial(self):
        return math.factorial(self.num)



class MyException(Exception):

    def __init__(self, message):
        self.message = message

    def msg(self):
        return self.message