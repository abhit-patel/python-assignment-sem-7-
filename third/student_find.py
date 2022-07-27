from secrets import choice
from tkinter import Menu


def add_student(name):
    f=open("student.txt","a")
    f.write(name+"\n")
    f.close()

def find_student(name):
    f=open("student.txt","r")
    lines=f.readlines()
    flag=0
    for i in lines:
        if i==name:
            return "student found"
    return " not found"
    

# f=open("student.txt","x")
# add_student("abhit hinsu")
# add_student("bhavy hinsu")
# add_student("vasu hinsu")
# add_student("anjali hingu")
# add_student("dev hingu")
# add_student("isha hingu")

# find_student("abhit hinsu")
# find_student("anjali hingu")

Menu = '''
  1. enter name to add in file :
  2. search name in file :
  3. exit
  ''' 
       
while(True):
    print(Menu)
    choice = input("enter your choice: ")
    if choice=='1':
        studentName= input("enter name: ")
        add_student(studentName)
    elif choice=='2':
        studentName= input("find name: ")
        find_student(studentName)
    elif choice=='3':
        print('exitng...')
        exit(0)
    else:
        print("enter right choice: ")


