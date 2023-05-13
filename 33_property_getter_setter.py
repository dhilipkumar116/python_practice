class student:
    def __init__(self,total):
        self._total =  total

    def average(self):
        return self._total/5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print('invalid input! value not changed')
        else:
            self._total = t;

inst = student(478)
print('total:',inst.total)
print('average:',inst.average())

inst.total = 600
print('total:',inst.total)
print('average:',inst.average())
