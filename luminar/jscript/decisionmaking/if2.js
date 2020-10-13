//check a number is palindrome or not
number=Number(prompt("enter the number"))
no=number;
rev=0;
while(number!=0){
reminder=number%10
rev=(rev*10)+reminder
number=parseInt(number/10)
}
if(rev==no){
alert("palindrome");
}
else{
alert("not palindrome");
}