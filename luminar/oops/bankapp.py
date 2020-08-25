import datetime
class Bank:
    #bnane="sbi" ///static variable
    def __init__(self,acno,pname):
        self.acno=acno
        self.pname=pname
        self.balance=3000
        self.bname="SBI"
    def deposit(self,amt):
        self.balance++amt
        print("your",self.bname,"has been credited with",amt,"on",datetime.date.today())
    def withdraw(self,amt):
        if(amt>self.balance):
            print("transaction has been cancelled error code 1101")
        else:
            self.balance+=amt
            print("your",self.bname,"has been debited with",amt,"on",datetime.date.today())
    def balanceEnquiry(self):
        print("your current available balance=",self.balance)
obj=Bank(1001,"anu")
obj.withdraw(1000)
obj.deposit(5000)
obj.balanceEnquiry()