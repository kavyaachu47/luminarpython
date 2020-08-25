#print frequent character
strg="ABABABCAA"
dic={}
for n in strg:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
print(dic)
rst=max(dic,key=dic.get)
print(rst)