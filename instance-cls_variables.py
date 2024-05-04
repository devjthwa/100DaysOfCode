class Employee:
    company = "Apple" # class variable
    noOfEmployees = 0
    def __init__(self,name):
        self.name = name
        self.raiseAmount = 0.02
        Employee.noOfEmployees +=1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the amount in {self.noOfEmployees} sized {self.company} is {self.raiseAmount}")
emp1 = Employee("Dev")
emp1.raiseAmount = 0.5
emp1.company = "Apple India"
emp1.showdetails()
emp2 = Employee("Devansh")
emp2.raiseAmount = 0.8
emp2.company = "Nestle India"
emp2.showdetails()
# Employee.showdetails(emp1)