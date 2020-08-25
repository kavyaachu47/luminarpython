num1=int(input("enter first number"))
num2=int(input("enter second number"))
lst=[1,2,3,4,5]
try:
    res=num1/num2
    print("result",res)
    print("file operation")
except Exception as e:
    num1=int(input("enter no"))
    num2=int(input("enter no"))
    try:
        res=num1/num2
        print("res=",res)
    except Exception as e:
        print(e.args)
finally:
    print("we have database transactions")