num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2)&(num1>num3)):#50>40 50>30
    if(num2>num3):#40>30
        print("num2 max",num2)#40
    else:
        print("num3 second largest",num3)
elif((num2>num1)&(num2>num3)):#55>50 55>40
    if(num1>num3):#50>40
        print("second largest",num1)#50
    else:
        print("second largest",num3)
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("second largest",num1)
    else:
        print("second largest",num2)
