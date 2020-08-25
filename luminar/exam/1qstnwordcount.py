#print word count
f=open("word","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(" ")
    print(words)
    for wrd in words:
        if(wrd not in dict):
            dict[wrd]=1
        else:
            dict[wrd]+=1
for k,v in dict.items():
    print(k,v)