f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num))
res=sum(lst)
print(res)