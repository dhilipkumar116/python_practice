import zope.interface

class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('foo')
    def method1(self, x):
        pass
    def method2(self):
        pass

@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self,x):
        return x+x
    def method2(self):
        return "foo"
obj = MyClass()
print(obj.method1(1))