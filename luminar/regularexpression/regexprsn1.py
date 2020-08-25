import re
matcher=re.finditer("ab","ababababababababbbabqbabba")
count=0
for match in matcher:
    print(match.start())#find position
    print(match.group())#find object match with
    count+=1
print(count)