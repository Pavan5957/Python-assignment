try:
    word = input("enter a word: ")
    flag = False
    for char in word:
        if char.isdigit():
            flag = True


    if flag:
        raise TypeError("please enter a valid word ")

    if len(word) > 50:
        raise ValueError("word is too long")

    print(word)

except TypeError as t:
    print(f"TypeError: {t}")

except ValueError as ve:
    print(f"error: {ve}")

