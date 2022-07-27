import pickle

def add_employee(empcode,name,salary):
    f=open("binary.dat","ab")
    record = {"empcode":empcode,"name":name,"salary":salary}
    pickle.dump(record,f)
    f.close()

def display_employee(sal):
    f=open("binary.dat","rb")
    while True:
        try:
            employee=pickle.load(f)
            if employee["salary"] > 30000:
                print(employee)
        except:
            break
    f.close()

empcode=int(input("Enter Code: "))
name=input("Enter name: ")
salary=int(input("Enter salary: "))
add_employee(empcode,name,salary)
sal=30000
display_employee(sal)