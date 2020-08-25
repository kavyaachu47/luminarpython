class Bank:
    def __init__(self,accno,personname,balance,bname):
        self.accno=accno
        self.personname=personname
        self.balance=balance
        self.bname=bname
    def printVal(self):
        print("ur accno is",self.accno)
        print("ur name",self.personname)
        print("ur balance",self.balance)
        print("ur bname",self.bname)
    def WithDraw(self):
        print("ur total amt=",self.balance)
        num=int(input("enter your amount want to withdraw"))
        if(num>self.balance):
            print("withdrawal notpossible")
        else:
            self.balance=self.balance-num
            print("ur current balance=",self.balance)
    def Deposit(self):
        self.num=int(input("enter ur amount want to deposit"))
        self.balance+=self.num
Accno=int(input("enter ur accountnumber"))
Name=input("enter ur name")
Balanc=1000
bname=input("enter ur bank name")
obj=Bank(Accno,Name,Balanc,bname)
i=1
print("1.Acoount details")
print("2.Deposit amount")
print("3.Withdraw")
print("4.Exit")
i=int(input("enter ur choice"))
while(i<4):
    if(i==1):
        obj.printVal()
    elif(i==2):
        obj.Deposit()
    elif(i==3):
        obj.WithDraw()
    else:
        break
    i=int(input("enter ur choice"))