lst=[10,10,20,20,30,31,31]
lst1=[]
lst.sort()
last=len(lst)
print(lst)
for i in range(0,last-1):
    t=lst[i]
    if(t!=lst[i+1]):
        lst1.append(t)
if(lst[last-2]==lst[last-1]):
    lst1.append(lst[last-1])
print(lst1)
