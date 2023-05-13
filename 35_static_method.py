class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetails(self):
        print("Name:",self.name,"age:",self.age)

    @staticmethod
    def collegeName(): #common to all instance
        print("MIT")

s1 = student("dhilip",34)
s1.printDetails()
s1.collegeName()
student.collegeName()