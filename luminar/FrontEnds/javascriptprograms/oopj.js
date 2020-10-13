class Person{
setPerson(id,name){
this.id=id;
this.name=name;
}
getPerson(){
console.log("name="+this.name);
console.log("id="+this.id);
}
}
let obj=new Person()
obj.setPerson(1001,"ajay");
obj.getPerson()