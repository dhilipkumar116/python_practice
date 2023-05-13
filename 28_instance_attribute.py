class Student:
    name="dhilip"

instance1 = Student()
print(Student.__dict__)
print(Student.name)
print(instance1.__dict__)
print(instance1.name)
# it checks for attribute inside instance1
# if not present , it will check into class.

instance1.name = 'kumar'
print('attribute inside instance1:',instance1.name)


instance2 = Student()
print(instance2.name)