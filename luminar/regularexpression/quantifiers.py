import re
#pattern="a" #checks a only
#pattern="a+" #occurance of a
#pattern="a*"#any no of a including 0 number of a
#pattern="a?"#individually checks each position
pattern="a{2}"#check for 2 no of a
#pattern="a{2,3}"#check for minimum 2 number of a max 3number of a
matcher=re.finditer(pattern,"abbabbaababaaabbb#@$")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("count",count)