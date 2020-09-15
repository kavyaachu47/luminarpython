f=open("employees","r")
emp={}
for lines in f:
    id,name,desig,sal=lines.rstrip("\n").split(",")
    if(id not in emp):
        emp[id]={"id":id,"name":name,"desig":desig,"sal":sal}
def fetchData(**kwargs):
    id=kwargs["id"]
    if(id not in emp):
        print("employe id not exist")
    else:

        print(emp[id]["name"])
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])
fetchData(id="1001",prop="sal")