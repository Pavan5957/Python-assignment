sentence = "Pavanlakmaje"

sentence = sentence.lower()
letter_counts = {}
for char in sentence:
    if char.isalpha():
        letter_counts[char] = sentence.count(char)
for letter , count in letter_counts.items():
    print(f"{letter} appears {count} times ")
max_count = max(letter_counts, key=letter_counts.get)
print(f"{max_count} is the most often letter ")


