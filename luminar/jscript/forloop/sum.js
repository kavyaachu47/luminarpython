var low=Number(prompt("enter lower"))
var upp=Number(prompt("enter upper"))
var esum=0
var osum=0

for(i=low;i<=upp;i++){
    if(i%2==0){
        esum+=i
        }
    else{
        osum+=i
}
        }
        console.log(esum);
        console.log(osum);