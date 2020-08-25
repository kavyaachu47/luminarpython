num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

first=0
second=0
third=0
if((num1>num2)&(num1>num3)):
    first=num1
    print(first)
    if(num2>num3):
        second=num2
        print(second)
    elif(num3>num2):
        third=num3
        print(third)
elif((num2>num1)&(num2>num3)):
    first=num2
    print(first)
    if(num1>num3):
        second=num1
        print(num1)
    else:
        print(num3)
elif ((num3>num1)&(num3>num2)):
    print(num3)
else:
    print("not in order")
