str1 = input("enter first string")
str2 = input("enter second string")
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for n in str1:
        if n in str2:
            flag = True
        else:
            flag = False
            break
        return flag


if anagram(str1, str2):
    print("anagram")
else:
    print(" not anagram")



