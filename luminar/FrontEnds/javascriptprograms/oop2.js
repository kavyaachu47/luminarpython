class Stud{
setStud(rol,name,tot){
this.rol=rol;
this.name=name;
this.tot=tot;
}
getStud(){
console.log("name="+this.name);
console.log("rol="+this.rol);
console.log("tot="+this.tot);
}
}
let obj=new Stud()
obj.setStud(1001,"Anoop",100);
obj.getStud()