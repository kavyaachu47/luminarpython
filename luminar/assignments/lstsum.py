lst=[]
n=int(input("enter 3 and enter 3 values for list="))
for j in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
lst1=[]
f=0
for i in lst:
    index=lst.index(i)
    if(index==0):
        f=lst[1]+lst[2]
        lst1.append(f)
    elif(index==1):
        f=lst[0]+lst[2]
        lst1.append(f)
    elif(index==2):
        f=lst[0]+lst[1]
        lst1.append(f)
    else:
        break
print(lst1)

