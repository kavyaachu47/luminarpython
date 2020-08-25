db=int(input("enter birth date"))
mb=int(input("enter birth month"))
yb=int(input("enter year of birth"))
cd=int(input("enter current date"))
cm=int(input("enter current month"))
age=cy-yb
if(mb>=cm):
    age=age-1
    if(bm==cm):
        if(db>cd):
            age=age-1
print("your age=",age,"years old")