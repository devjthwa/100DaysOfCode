'''class EMployee:
    def __init__(self):
        # self.name = "dev"
        self.__name = "dev"

a= EMployee()
# print(a.name)
# print(a.__name) cant be accessed
print(a._EMployee__name)
print(a.__dir__())
'''
# 2nd -----------------
class Student():
    def __init__(self):
        self._name = "Harry"

    def _funName(self): # protected method
        return "Dev Jethwa"
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())
    