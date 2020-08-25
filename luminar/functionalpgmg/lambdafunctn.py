#lambda----->

f=lambda num1,num2:num1+num2
print(f(10,20))

f1=lambda num1,num2:num1-num2
print(f1(40,20))

f2=lambda num1,num2:num1*num2
print(f2(10,20))

#map ------>

lst=[1,2,3,4]
def square(num):
    return num*num
sq=list(map(square,lst))
print(sq)

#filter----->

def even(num):
    return  num%2==0
even=list(filter(even,lst))
print(even)
