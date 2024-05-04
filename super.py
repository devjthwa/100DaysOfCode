'''class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def parent_method(self):
        print("Dev")
    def child_method(self):
        print("Child method")
        super().parent_method()

child_obj = Child()
child_obj.parent_method()
child_obj.child_method()'''

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,language):
        self.language = language
        super().__init__(name,id)

dev = Employee("Dev", 340)
dev2 = Programmer("Dev2", 341, "Development")

print(dev2.name)
print(dev2.id)
print(dev2.language)