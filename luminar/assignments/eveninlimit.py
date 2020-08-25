low=int(input("enter a lower limit"))
upper=int(input("enter a upper limit"))
for i in range(low,(upper+1)):
    if(i%2==0):
        print(i)