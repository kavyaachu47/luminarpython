from re import *
f=open("mailids", "r")
list=[]
rule='\w*[@]gmail.com'
for lines in f:
    dat=lines.rstrip("\n")
    match=fullmatch(rule,dat)
    if(match!=None):
        print("valid mail id=",dat)
        list.append(dat)
    else:
        print("invalid mailid")

#to open correct ids in another file:->

f1=open("checked","w")
for i in list:
    f1.write(i)
f1=open("checked","r")
print("correct ids are=")
for data in f1:
    print(data)