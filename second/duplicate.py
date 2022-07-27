# list1 = []
# n = int(input("length of list = "))

# for i in range (0 ,n):
#     ele = int(input())
#     list1.append(ele) 

# print( list1)

# new_list = list(set(list1))

# print( new_list)





#simple way

list1 = []
n = int(input("length of list = "))

for i in range (0 ,n):
    ele = int(input())
    list1.append(ele) 

print(list1)

res= []

for i in list1:
    if i not in res:
        res.append(i)

print(res)
