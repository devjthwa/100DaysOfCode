class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Lion:
    def __init__(self,hunt):
        self.hunt = hunt
    def show(self):
        print(f"The hunt is {self.hunt}")

class LionAnimal(Lion, Animal):
    def __init__(self,name,hunt):
        self.name = name
        self.hunt = hunt

m = LionAnimal("Mufasa", "Deer")
print(m.name, m.hunt)
m.show()

print(LionAnimal.mro())