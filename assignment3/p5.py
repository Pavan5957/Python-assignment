def pangram(sentence):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())

    return sentence_set.issubset(alphabet_set)


new_str = input("enter a string")
if pangram(new_str):
    print("pangram")
else:
    print("not pangram")
