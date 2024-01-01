str = input("enter a string")

new_str = []
duplicate_characters = []
flag = None
def duplicate(str, new_str):
    global flag
    for n in str:
        if n not in new_str:
            new_str.append(n)
        else:
            global duplicate_characters
            duplicate_characters.append(n)


duplicate(str, new_str)
if len(duplicate_characters) == 0:
    print("no duplicate characters")
else:
    print(duplicate_characters)




