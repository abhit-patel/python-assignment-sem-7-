f=open("abc.txt","r")
n = f.read()
c=0

for i in n:
        if i.isupper():
            c+=1
print(c)