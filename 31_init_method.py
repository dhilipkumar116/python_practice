class user:
    def __init__(self,name):
        print("init is a constructor method")
        self.name = name
    def printAll(self):
        print(self.name)

inst1 = user('dhilip')
inst1.printAll()
print(inst1.__dict__)
print(user.__dict__)
