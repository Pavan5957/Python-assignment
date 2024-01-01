str = input("enter a string")
print(str[::-1])
if str == str[::-1]:
    print("given string is palindrome")
else:
    print("string is not palindrome")
