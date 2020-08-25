lst=[1,2,3,4,5]
ele=int(input("enter value"))#4
lst.sort()
low=0
upp=len(lst)-1#
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==ele):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>ele):
        upp=upp-1
    else:
        low=low-1