class Dada:
    def __init__(self,eat,sleep):
        self.eat = eat
        self.sleep = sleep
    def show(self):
        print(f"Eat : {self.eat}")
        print(f"sleep : {self.sleep}")

class Pita(Dada):
    def __init__(self,eat,earn):
        Dada.__init__(self,eat,sleep = "3hr")
        self.earn = earn
    def show(self):
        Dada.show(self)
        print(f"Earn : {self.earn}")
class Beta(Pita):
    def __init__(self,eat,learn):
        Pita.__init__(self,eat,earn = "20k")
        self.learn = learn
    def show(self):
        Pita.show(self)
        print(f"Learn : {self.learn}")

o = Beta("Food", "Python")
o.show()
print(Beta.mro())