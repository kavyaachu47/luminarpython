#Program to check if a sequence is palindrome?

n=int(input("enter a value"))#121
t=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(t==rev):
    print("is Palindrome")
else:
    print("not a palindrome")
