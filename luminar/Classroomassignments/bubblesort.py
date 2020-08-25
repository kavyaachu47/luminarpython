#pprogram to implement bubble sort
lst=[]
n=int(input("enter the list limit"))
print("enter list elements")
for i in range(0,n):
    lst.append(int(input()))
print("unsorted",lst)
for i in range(0,n-1):
    for j in range(0,n-1):
        if(lst[j]>lst[j+1]):
            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
print("sorted",lst)