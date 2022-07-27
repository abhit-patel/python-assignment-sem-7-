def bublesort(n):
 l=len(n)
 for i in range (l):
     for j in range (l-i-1):
         if n[j] > n[j+1]:
             n[j],n[j+1]=n[j+1],n[j]

n=[1,8,3,9,12,4,72]
bublesort(n)
print("Sorted elemts are: ")
for i in range(len(n)):
    print(n[i],end=" ")