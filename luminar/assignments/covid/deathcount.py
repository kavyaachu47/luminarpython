f=open("covid_19_india.csv","r")
dict={}
dict1={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    confirmed=data[6]
    print(state,",",death)
    if(state not in dict):
        dict[state]=death
        dict1[state] = confirmed
    else:
        dict[state]=death
        dict1[state] = confirmed
deathsum = 0
consum = 0
dlist=[]
clist=[]
for k,v in dict.items():
    dlist.append((int(v)))
    deathsum+=int(v)
    print(k,",",v)
for k, v in dict.items():
    if(max(dlist)==int(v)):
        print("highest death=",k,v)
for k, v in dict1.items():
    clist.append(int(v))
    consum += int(v)
for k, v in dict1.items():
    if (max(clist) == int(v)):
        print("highest confirmed=", k, v)
print("total death=",deathsum)
print("total confirmed=",consum)