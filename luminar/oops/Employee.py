class Employee:
    def __init__(self,Eid,Ename,Desig,Salary):
        self.Eid=Eid
        self.Ename=Ename
        self.Designation=Desig
        self.Salary=Salary
    def printValue(self):
        print("ur id is",self.Eid)
        print(self.Ename)
        print(self.Designation)
        print(self.Salary)

ob=Employee(1,"raghu","manager",15000)
ob.printValue()
print("*******************")

class Person:
    def __init__(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def printValues(self):
        print(self.age)
        print(self.name)
        print(self.gender)
obj=Person(27,"happy","male")
obj.printValues()