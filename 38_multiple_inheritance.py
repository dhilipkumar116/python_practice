class father:
    def fishing(self):
        print("fishing from father")
    def chess(self):
        print("chess from father")


class mother:
    def dancing(self):
        print("dancing from mother")

    def chess(self):
        print("chess from mother")

# order of execution is depends on order of parameters
class son(father,mother):
    def ride(self):
        print("i am riding bike")

s1 = son()

s1.fishing()
s1.chess()
s1.ride()
