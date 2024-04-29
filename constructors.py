class Person:
    def __init__(self,name,occ):
        print("constuctor called")
        self.name = name
        self.occ = occ


    def info(self):
        print(f"{self.name} is a {self.occ}")

# a = Person()
# a.name = "Div"
# a.occ = "HR"
# a.info()
a = Person("Dev", "Developer")
c = Person(1,2)
a.info()
c.info()