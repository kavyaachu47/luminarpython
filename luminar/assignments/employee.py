import functools


class Emp:
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.desi=designation
        self.salary=int(salary)
    def printEp(self):
        print("name=", self.name)
        print("designation=", self.desi)
        print("Salary=",self.salary)
    def __str__(self):
        return self.name

f=open("edtl","r")
elst=[]

for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desi=values[2]
    salary=values[3]
    obj=Emp(id,name,desi,salary)
    obj.printEp()
    elst.append(obj)
    n=5000

for emp in elst:
    uppr=list(map(lambda emp:emp.name.upper(),elst))
    incr=list(map(lambda emp:emp.salary+n,elst))
    grtr=list(filter(lambda obj:obj.salary>25000,elst))
print("uppr")
for i in uppr:
    print(i)
print("increment")
for i in incr:
    print(i)
for i in grtr:
    print(i)
maxsal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.salary,elst)))
print(maxsal)

equals=list(filter(lambda emp:emp.salary==maxsal,elst))
for eq in equals:
    print(eq)