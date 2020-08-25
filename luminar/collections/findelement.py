lst=[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("enter an element"))
flg=0
for i in lst:
    if(i==element):
        flg+=1
        break
    else:
        pass
if(flg>0):
        print("element found")
else:
        print("not found")
