///HHHPPSDAAA->3H2P1S1D3A
var str="HHHPPSDAAA"
var countc={}
for (ch of str){
if(ch in countc){
countc[ch]+=1;
}
else{
countc[ch]=1;
}
}
var output=""
for(key in countc){
output=output+countc[key]+key
}
console.log(output)