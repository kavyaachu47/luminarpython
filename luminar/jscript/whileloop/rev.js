//reverse a number
var n=Number(prompt("enter a no"))
var res=0
while(n!=0){
    dig=n%10
    res=(res*10)+dig
    n=parseInt(n/10)
    }
alert(res);
