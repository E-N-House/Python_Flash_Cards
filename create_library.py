import pandas
from tkinter import messagebox
DATA_FILE = "french_to_learn.csv"

DataFrame = pandas.read_csv("data/french_words.csv")
# translates the data to a list containing dictionaries for each word
data = DataFrame.to_dict(orient="records")

def create_data_file():
    """checks if a file exists. And if it doesn't create a text file using global constant DATA_FILE
    and fills in the column names as top row separated by spacer"""
    try:
        file = open(DATA_FILE)
    except FileNotFoundError:
        messagebox.showinfo(title="Creating File", message=f"Creating a file named {DATA_FILE}\n"
                                                           f"to store your information.")
        file = open(DATA_FILE, mode="r")
        file.write(data)
    finally:
        file.close()


learning_data = create_data_file()

