class student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count = student.count+1

    def printDetails(self):
        print("name:",self.name," age:",self.age)

    @classmethod
    def total(cls):
        return cls.count

inst = student("dhilip",22)
inst.printDetails()
inst1 = student("kumar",11)
inst1.printDetails()
print("total :",student.count)