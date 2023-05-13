
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.msg = self.name+" is "+str(self.age)+" yr old."

    # def msg(self):
    #     return self.name+" is "+str(self.age)+" yr old."

    @property
    def msg(self):
        return self.name+" is "+str(self.age)+" yr old."


inst = user("dhilip",22)
print(inst.name)
print(inst.age)
print(inst.msg)

# # setting new value to the age variable
# print('after updating age value-----------------------')
# inst.age = 50
# print(inst.name)
# print(inst.age)
# print(inst.msg) #msg is not updating

# # to display updated valued we have to return msg from function
# print('after updating age value using function------------')
# inst.age=50
# print(inst.name)
# print(inst.age)
# print(inst.msg())
#

# if msg looks like function it creates confusion
# so we are using property decorator
print('updated value using propery decorator-----------')
inst.age=50
print(inst.name)
print(inst.age)
print(inst.msg)


