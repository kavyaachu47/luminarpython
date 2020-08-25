
n=3
lst=[]
print("enter your list")
for i in range(0,n):
    lst.append(input())
lst1=[]
m=len(lst)-1
for i in range(0,m):
    res=lst[i],lst[i+1]
    if res != lst1:
        lst1.append(res)
    res1=lst[0],lst[m]
    if res1 != lst1:
        lst1.append(res1)
print(lst1)

