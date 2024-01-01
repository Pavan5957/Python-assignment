str = input("enter a string")

frequent_characters = {}
for n in str:
    frequent_characters[n] = str.count(n)
print(frequent_characters)

frequent_character = max(frequent_characters, key=frequent_characters.get)
print(f"frequent character is {frequent_character}")

