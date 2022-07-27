def square(r):
   for i in range(1,r+1):
      for j in range(1,11):
         print(i*j, end="  ")
      print("")

a=int(input("Enter input 1: "))
square(a)