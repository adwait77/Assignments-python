class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c

    def display(self):
        print("class A:")
        print("value of a:",self.__a)
        print("value of b:",self._b)
        print("value of c:",self.c)

class B(A):
    def display(self):
        try:
            print("class B:")
            print("value of a:",self.__a)
        except AttributeError:
            print("Cannot access private member a in class B")
        print("value of b:",self._b)
        print("value of c:",self.c)


obj1=B(10,20,30)
obj1.display()
