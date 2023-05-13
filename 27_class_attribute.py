class Student:
    '''sample doc string'''
    name="dhilip"
    age=22
    def func(self):
        print('adf')

# two methods
# get attribute(inbuild function)
# dot notation
# get attribute
print(getattr(Student,'name'))
print(getattr(Student,'age'))
print(getattr(Student,'func'))

# print(getattr(Student,'gender'))
# gives error bcoz no such attribute present
# to prevent that error
print(getattr(Student,'gender','no such attribute present'))

#got notation
print(Student.name)
print(Student.age)

#set attribute
print('setattr---------------')
setattr(Student,'name','kumar')
print(Student.name)

setattr(Student,'city','chengapattu')
print(Student.city)

# del attribute
print('del attribute-------------')
delattr(Student,'city') # or del Student.city
print(Student.__dict__)
print(Student.__doc__)
