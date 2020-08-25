#divide(10,3)=>(3,1) not using /%
x=10
y=3
for i in range(1,9):
    if y*i>x:
        break
z=i-1
print("quotient=",z)
print("reminder=",(x-(y*z)))
