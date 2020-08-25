class Parent:
    def m1(self):
        print("inside parent1")

class Child:
    def m2(self):
        print("inside child")

class SubChild(Child,Parent):
    def m3(self):
        print("inside subchild")

p=Parent()
p.m1()
s=SubChild()
s.m3()
s.m2()
s.m1()