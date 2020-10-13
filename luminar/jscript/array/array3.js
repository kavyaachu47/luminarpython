var arr=[1,2,3,4,5,6,7,8,9,10,11,12]
var element=Number(prompt("enter an element"))
flg=0
for (i in arr){
    if(i==element){
        flg+=1
        break
        }
    else{
        flg=0
        }
        }
if(flg>0){
       alert("element found");
       }
else{
        alert("not found");
        }

