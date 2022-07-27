def multiple(x,y):
    ans =0
    for i in range(1,y+1):
        ans = ans+x
    print(ans)

a = int(input("enter first value= "))
b = int(input("enter second value= "))
multiple(a,b)