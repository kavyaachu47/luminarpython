employee={"eid":1002,
          "ename":"person",
          "desi":"tester",
          "sal":15000
          }
print(employee["ename"])
print("companyname"in employee)
employee["companyname"]="Luminar"
print(employee["companyname"])
employee["sal"]+=5000
print(employee["sal"])
for key in employee:
    print(key,"",employee[key])