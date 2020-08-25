lst=[10,11,12,14,13,15,3,2,4]
lst.sort()
print(lst)#[2,3,4,10,11,12,13,14,15]
low=0
upp=len(lst)-1#9-1=8
element=int(input("enter number to search"))#14
flg=0
while(low<=upp):#0<=8
    mid=(low+upp)//2#0+8//2=4(11)
    if(element>lst[mid]):#14>11
        low=mid+1#4+1=5
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if(flg>0):
    print("element found")
else:
    print("not found")