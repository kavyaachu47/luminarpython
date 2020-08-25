class Person:
    def setValues(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def printValues(self):
        print(self.age)
        print(self.gender)
        print(self.name)
obj=Person()