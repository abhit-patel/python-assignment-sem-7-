sen = input("enter string= ")
word =sen.split(" ")
print("length of words :" , len(word))
print("length of string" , len(sen))

count = 0
for i in range(0,len(sen)):
    if(sen[i].isalnum()):
        count+= 1

print("percentage = " , (count*100)/len(sen))