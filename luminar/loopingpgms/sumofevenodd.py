low=int(input("enter lower"))
upp=int(input("enter upper"))
esum=0
osum=0

for i in range(low,(upp+1)):
    if(i%2==0):
        esum+=i
    else:
        osum+=i

        print(esum)
        print(osum)