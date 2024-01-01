import pandas
data = pandas.read_csv("french_words.csv")
data = data.to_dict(orient="records")
print(data)

