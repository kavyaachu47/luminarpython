var num=[10,20,30,40,50,60];
console.log(num[0]);

num[0]=100;
for(item of num){
console.log(item)
}

num.push(500);
console.log(num)