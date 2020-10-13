//factorial
var numbr=Number(prompt("enter number"))
var f=1
var i=2
function facto(numb){
while(i<=numbr){
f*=i
i++
}
return(f)
}
var d=facto(numbr)
alert("factorial-"+d);