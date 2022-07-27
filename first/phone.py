

# def dsh(s,i):
#     return s[:i]+ '-'+ s[i:]

# p=input("Enter your mobile no.: ")
# l=len(p)
# if l > 10 or l < 10:
#     print("It is not a valid no.")
# else:
#     p=dsh(p,3)
#     p=dsh(p,7)
#     print("Formated no.: ",p)


p=int(input("enter phone number= "))
l=len(p)
if l > 12 or l < 12:
    print("It is not a valid no.")
elif( p[1:3] + '-'+ p[5:7]+'-' + p[9:12]):
    print("vaild")
else:
    print("invaild")
