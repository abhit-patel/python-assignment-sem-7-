import time
l=[]
m = []
with open("fy.txt") as f :
    for i in f:
        for a in i.strip().split():
            l.append(a)
            m+= a
print(l)