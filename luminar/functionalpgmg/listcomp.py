lst=[1,2,3,4,5]
sq=[(i+i)for i in lst]
print(sq)
##
pairs=[(i,j)for i in lst for j in lst]
print(pairs)
##
odd=[i for i in lst if i%2==0]
print(odd)