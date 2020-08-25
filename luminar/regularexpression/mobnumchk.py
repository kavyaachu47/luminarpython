from re import *
#rule="[9][1]\d{10}"
rule="\d{10}"
mobnumbr=input("enter mob no")
matcher=fullmatch(rule,mobnumbr)
if(matcher!=None):
    print("valid mobile no")
else:
    print("invalid")