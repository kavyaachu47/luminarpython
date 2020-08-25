lowr=10
upr=50

for i in range(lowr,(upr+1)):
    if(i>1):
         for n in range(2,(i+1)):
             if(i%n==0):
                 break
             else:
                print(i)

