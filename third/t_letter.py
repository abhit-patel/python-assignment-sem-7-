f=open("story.txt",encoding="utf8")
n = f.readlines()
c=0
for i in n:
    if (i[0]=='t')or(i[0]=='T'):
        continue
    else :
        c=c+1
print(c)