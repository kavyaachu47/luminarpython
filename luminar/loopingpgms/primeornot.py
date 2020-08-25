no=int(input("enter a number"))
flg=0
for i  in  range(2,no):
    if(no%i==0):
        flg=1
        break
    else:
        flg=0
if(flg>0):
    print("not prime")
else:
    print("prime")