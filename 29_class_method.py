class Student:
    name = "dhilip"
    age = 22
    def __init__(self):
        self.__a = 10

    def printAll():
        print("Name :", Student.name)
        print("Age  :", Student.age)




Student.printAll()
print(Student.name)
print(Student.__dict__)

Student.__dict__['printAll']()

# can access the private member using special syntax
obj1 = Student()
print(obj1._Student__a)
