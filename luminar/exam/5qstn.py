#[1,2,3,4]=>6=>(2,4)
lst=[1,2,3,4]
el=int(input("enter element"))
lst.sort()
low=0
up=len(lst)-1
while(low<=up):
    value=lst[low]+lst[up]
    if(value==el):
        print("pair is",lst[low],lst[up])
        break
    elif(value>el):
        up=up-1
    else:
        low=low+1
