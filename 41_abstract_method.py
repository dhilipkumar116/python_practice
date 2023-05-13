from abc import ABC,abstractmethod
# ABC - Abstract Base Class

class Bank(ABC):

    # method declaration
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def credit(self):
        pass
    @abstractmethod
    def debit(self):
        pass

class HDFC(Bank):

    def loan(self):
        print("providing loan")

    def credit(self):
        print("providing credit card")

    def debit(self):
        print("providing debit card")

hdfc = HDFC()
hdfc.loan()
hdfc.credit()
hdfc.debit()

