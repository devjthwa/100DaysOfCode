class Person:
    name = "dev"
    occupation = "programmer"
    netWorth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a= Person()
a.name = "Devang"
a.occupation = "CA"

b= Person()
b.name = "Nitika"
b.occupation = "HR"

# print(a.name + " "+ a.occupation)
a.info()
b.info()