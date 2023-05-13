class A:
    def display(self):
        print("i am from class A")

class B(A):
    def display(self):
        print("i am from class B")

class C(A):
    def display(self):
        print("i am from class C")

class D(B,C):
    # def display(self):
    #     print("i am from class D")
    pass

inst = D()
inst.display()