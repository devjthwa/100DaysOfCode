class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"The name of the employee is {self.name} and id is {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

e = Employee("dev",678)
e.showdetails()
e2 = Programmer("dev",688)
e2.showdetails()
e2.showLanguage()
# e.showLanguage() gives error
