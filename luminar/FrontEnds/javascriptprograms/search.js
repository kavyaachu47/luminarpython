var num=[10,20,30,40,50,60];
var ele=40;
var flag=0;
for(item of num){
if(item==ele){
flg+=1;
break;
}
else{
flg=0;
}
}
if(flg>0){
console.log("element found")
}
else{
console.log("not found")
}