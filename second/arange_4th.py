
def  anagrams(str1,str2):
    if(sorted(str1) == sorted(str2)):
        # return True
        return ('it is a  anagrams sentence')
    else:
        # return False
        return ('it is not a anagrams sentence')

string1 = input("enter first string = ")
string2 = input("enter first string = ")

print( anagrams(string1, string2))
