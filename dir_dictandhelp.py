x = [1,2,3]
print(dir(x))
print(x.__add__)
class Test:
    def __init__(self,name):
        self.name = "Dev"

e1 = Test("Dev")
print(e1.__dict__)
print(help(Test))