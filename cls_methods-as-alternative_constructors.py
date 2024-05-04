class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromString(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e = Employee("dev",12000)
print(e.name)
print(e.salary)

# string = "devang-112000"
# e2 = Employee(string.split("-")[0],string.split("-")[1])
# print(e2.name)
# print(e2.salary)

string = "devang-112000"
e2 = Employee.fromString(string)
print(e2.name)
print(e2.salary)
