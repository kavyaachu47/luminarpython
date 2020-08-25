from re import *
list=[]
rule='[kK][lL][0-9]{2}[a-z]{2}\d{4}'
f=open("regno","r")
for lines in f:
    data=lines.rstrip("\n")
    match=fullmatch(rule,data)
    if (match != None):
        print("Va0lid reg no",data)
        list.append(data)
    else:
        print("invalid reg no",data)



