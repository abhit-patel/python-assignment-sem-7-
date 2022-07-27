def sorted(li):
    for i in range (len(li)):
        if li[i] > li[i+1]:
            return False
        return True

list = [2,6,41,324,678]

print(sorted(list))



