# Write a program to check if two strings are a rotation of each other?

def arr_rotational (str1,str2):
    if len(str1) != len(str2):
        return False
    concatenated = str1 + str1
    return str2 in concatenated
str1 = input("Enter your str1 : ")
str2 = input("Enter your str2 : ")
if arr_rotational(str1,str2):
    print("Print str1 and str2 are rotation of each other")
else:
    print("Each strings are not rotationals")
