import pandas
from tkinter import messagebox
DATA_FILE = "data/french_to_learn.csv"
SEED_LIST_FILE = "data/french_words.csv"


def access_data_file():
    """Check if a file exists. If not, create it and fill in the column names as top row."""
    try:
        pandas.read_csv(DATA_FILE)
    except FileNotFoundError:
        messagebox.showinfo(title="Creating File", message=f"Creating a file named {DATA_FILE}\n"
                                                           f"to store your information.")
        start_data = pandas.read_csv(SEED_LIST_FILE)
        start_data.to_csv(DATA_FILE, index=False)


def update_data_file(card):
    """Access current learning list and updates lang_to_learn.csv by removing known cards"""
    global learning_data
    learning_data.remove(card)
    # Chains creating dataframe and then creating updated csv file together
    pandas.DataFrame(learning_data).to_csv(DATA_FILE, index=False)


# Check if the data file exists, and create it if necessary
access_data_file()

# Read the data from the CSV file
current_DataFrame = pandas.read_csv(DATA_FILE)

# Translates the data to a list containing dictionaries for each word
learning_data = current_DataFrame.to_dict(orient="records")
