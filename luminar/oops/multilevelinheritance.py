class Parent:
    def m1(self):
        print("inside parent1")

class Child(Parent):
    def m2(self):
        print("inside child")

class SubChild(Child):
    def m3(self):
        print("inside subchild")
su=SubChild()
su.m1()
su.m2()
su.m3()
ch=Child()
ch.m2()
ch.m1()
obj=Parent()
obj.m1()
