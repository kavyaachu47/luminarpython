//function factorial(n)
//{
//if(n==0||n==1){
//return 1;
//}
//else{
//return n*factorial(n-1);
//}
//}
//var n=5;
//res=factorial(n)
//console.log(res)
function factorial(num){
var i=1;
var fact=1;
while(i<=num){
fact=fact*i;
i+=1;
}
console.log(fact)
}