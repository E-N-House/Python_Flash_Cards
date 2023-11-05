import pandas

DataFrame = pandas.read_csv("data/french_words.csv")
# translates the data to a list containing dictionaries for each word
data = DataFrame.to_dict(orient="records")
