#Program to produce fibonacci series

num=int(input("enter value"))
a=0
b=1
sum=0
c=1
while(c<=num):
    print(sum,end="")
    c+=1
    a=b
    b=sum
    sum=a+b