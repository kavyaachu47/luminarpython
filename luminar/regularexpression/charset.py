from re import *
#patterns='[abc]'#check either a,b or c
#pattern='[a-z]'#it will check for character in lowercase a to z
#pattern='[A-Z]'
#pattern='[a-zA-Z]'
#pattern='[a-kA-Z]'
#pattern='[0-9]'
#pattern="\s"
#pattern="\d"
#pattern="\D"
#pattern="\w"
pattern="\W"
matcher=finditer(pattern,"abx 7Zxy@")
count=0
for match in matcher:
    print(match.start())
    print(match.group())