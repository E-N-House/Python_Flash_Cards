import pandas
from tkinter import messagebox
DATA_FILE = "data/french_to_learn.csv"


def access_data_file():
    """checks if a file exists. And if it doesn't create a text file using global constant DATA_FILE
    and fills in the column names as top row separated by spacer"""
    try:
        file = open(DATA_FILE)
    except FileNotFoundError:
        messagebox.showinfo(title="Creating File", message=f"Creating a file named {DATA_FILE}\n"
                                                           f"to store your information.")
        start_list = open("data/french_words.csv")
        start_data = start_list.read()
        # leave this as is if it is changed to utf-8 it shifts french lang characters to unicode
        file = open(DATA_FILE, mode="w")
        file.write(start_data)
        start_list.close()
    finally:
        file.close()


def update_data_file(card):
    global learning_data
    # global DataFrame
    learning_data.remove(card)
    new_dataframe = pandas.DataFrame(learning_data)
    update_data = new_dataframe.to_csv(index=False)
    # Use utf-8 to mitigate parsing errors in pandas caused by french unique characters
    file = open(DATA_FILE, mode="w",  encoding='utf-8')
    file.write(update_data)
    file.close()


access_data_file()
DataFrame = pandas.read_csv(DATA_FILE)

# translates the data to a list containing dictionaries for each word
learning_data = DataFrame.to_dict(orient="records")
#



