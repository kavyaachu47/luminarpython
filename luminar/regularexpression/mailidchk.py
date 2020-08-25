from re import *
#kavyarkairali@gmail.com
rule='\w[@]gmail.com'
mailid=input("enter gmailid")
matcher=fullmatch(rule,mailid)
if(matcher!=None):
    print("Valid id")
else:
    print("invalid id")