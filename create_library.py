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
        file = open(DATA_FILE, mode="w")
        file.write(start_data)
        start_list.close()
    finally:
        file.close()


test_card = {'French': 'partie', 'English': 'part'}


def update_data_file(card):
    global learning_data
    learning_data.remove(card)
    print(learning_data)
    update_data = pandas.DataFrame.to_csv(learning_data)
    print(update_data)
    file = open(DATA_FILE, mode="w")
    # file.write(learning_data.)
    file.close()


access_data_file()
DataFrame = pandas.read_csv(DATA_FILE)

# translates the data to a list containing dictionaries for each word
learning_data = DataFrame.to_dict(orient="records")
update_data_file(test_card)



