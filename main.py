from tkinter import *
# import json
# import pandas

from button_clicks import *
from create_card import choose_word


LEARNING_LANGUAGE = "Français"
BASE_LANGUAGE = "English"
PROJECT_NAME = f"Flash Cards {LEARNING_LANGUAGE}/{BASE_LANGUAGE}"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
PADDING_WINDOW = 0
BACKGROUND_COLOR = "#B1DDC6"
COLOR_SECOND = "yellow"
COLOR_THIRD = "#e2979c"
COLOR_ERRORS = "#e7305b"
ERROR_FONT = ("Arial", 20, "bold")

WORD_FONT = ("Arial", 26, "bold")
WORD_TEXT_COLOR = "white"
WORD_BG_COLOR = "light blue"

LANGUAGE_FONT = ("Arial", 16, "italic")


# ---------------------------- BUTTON VARIABLES--------------------------- #
CORRECT_BG_COLOR = "green"
INCORRECT_BG_COLOR = "red"

BUTTON_FONT = ("Arial", 26, "bold")
BUTTON_TEXT_COLOR = "white"
BUTTON_BG_COLOR = "light blue"

BUTTON_COLUMN_START = 0
BUTTON_ROW_START = 3

BUTTON_PAD_Y = 10
BUTTON_PAD_X = 10

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2

# ---------------------------- CARD VARIABLES--------------------------- #
CARD_FRONT_FILE = "images/card_front.png"
CARD_BACK_FILE = "images/card_back.png"

CARD_WIDTH = 800
CARD_HEIGHT = 526

DATA_FILE = "pw_data.json"

# ---------------------------- UI SETUP ------------------------------- #


# creating tk window
window = Tk()
window.config(bg=BACKGROUND_COLOR, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pady=PADDING_WINDOW,
              padx=PADDING_WINDOW)
window.title(PROJECT_NAME)

# Creating canvas
canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background=BACKGROUND_COLOR,
                highlightthickness=0, )
# adding IMAGE Card to middle of screen using a grid system
card_front_img = PhotoImage(file=CARD_FRONT_FILE)
back_card_img = PhotoImage(file=CARD_BACK_FILE)
current_word = choose_word()
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=card_front_img,)
canvas.create_text([WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5], text=LEARNING_LANGUAGE, font=LANGUAGE_FONT)
canvas.create_text([WINDOW_WIDTH/2, WINDOW_HEIGHT/2], text=current_word, font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# FORM LABELS


# BUTTONS
correct_button = Button(text="✔", background=CORRECT_BG_COLOR, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                        fg=BUTTON_TEXT_COLOR, font=BUTTON_FONT, command=correct_clicked)
correct_button.grid(column=BUTTON_COLUMN_START, row=BUTTON_ROW_START, )

incorrect_button = Button(text="❌", background=INCORRECT_BG_COLOR, fg=BUTTON_TEXT_COLOR, font=BUTTON_FONT,
                          height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=incorrect_clicked)
incorrect_button.grid(column=BUTTON_COLUMN_START+1, row=BUTTON_ROW_START, pady=BUTTON_PAD_Y,
                      padx=BUTTON_PAD_X,)

window.mainloop()
