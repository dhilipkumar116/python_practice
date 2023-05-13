
class PowTwo:

    def __init__(self, max=0):
        self.n = 0
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

pow = PowTwo(3)
iterator = iter(pow)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in PowTwo(3):
    print(i)



