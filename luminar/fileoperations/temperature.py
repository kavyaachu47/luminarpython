f=open("temoeraturedata","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    district=data[0]
    temoeraturedata=data[1]
    print(district)
    print(temoeraturedata)
    if(district not in dict):
        dict[district]=temoeraturedata
    else:
        old=dict[district]
        if temoeraturedata>old:
            dict[district]=temoeraturedata
print(dict)