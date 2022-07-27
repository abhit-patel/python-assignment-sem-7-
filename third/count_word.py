f=open("words.txt","r")
n = f.read()
c=1
for i in n:
        if i==" ":
            c=c+1
print(c)