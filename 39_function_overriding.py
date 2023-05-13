class Employee:
    def workingHrs(self):
        self.hrs = 8

    def printHrs(self):
        print("working hrs:",self.hrs)

class Trainee(Employee):
    def workingHrs(self):
        self.hrs = 20

    def resetHrs(self):
        super().workingHrs()

e1 = Employee()
e1.workingHrs()
e1.printHrs()

t1 = Trainee()
t1.workingHrs()
t1.printHrs()

print("reseting hrs----------------")
t1.resetHrs()
t1.printHrs()
