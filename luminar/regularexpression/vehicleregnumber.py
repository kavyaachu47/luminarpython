from re import *
rule='[K][L][0-9]{2}[a-z]{1,2}\d{4}'
regno=input("enter registration number")
matcher=fullmatch(rule,regno)
if(matcher!=None):
    print("Valid reg no")
else:
    print("invalid reg no")