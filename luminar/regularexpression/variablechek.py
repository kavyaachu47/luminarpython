#1)first alphabet of variablename is in betwen a-breakpoint
#2)second must be a number divisible by 3
#3)third must be any number of characters


from re import *

rule='[a-k][369][a-zA-Z0-9]*'

varname=input("enter variable name")
matcher=fullmatch(rule,varname)

if(matcher!=None):
    print("Valid")
else:
    print("Invalid")