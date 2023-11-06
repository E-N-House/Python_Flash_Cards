from tkinter import *
# import json
from create_card import choose_learning_card
from button_clicks import *

LEARNING_LANGUAGE = "Français"
BASE_LANGUAGE = "English"
PROJECT_NAME = f"Flash Cards {LEARNING_LANGUAGE}/{BASE_LANGUAGE}"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 526
PADDING_WINDOW = 50
BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 30, "bold")
LEARNING_LANG_TEXT_COLOR = "black"
BASE_LANG_TEXT_COLOR = "white"

TIMER = 3000

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


def flip_card():
    canvas.itemconfig(language_text, text="English", fill=BASE_LANG_TEXT_COLOR)
    canvas.itemconfig(current_text, text=current_card["English"], fill=BASE_LANG_TEXT_COLOR)
    canvas.itemconfig(card_image, image=card_back_img)


def change_word():
    global current_card
    current_card = choose_learning_card()
    learning_word = current_card["French"]
    canvas.itemconfig(language_text, text=LEARNING_LANGUAGE, fill=LEARNING_LANG_TEXT_COLOR)
    canvas.itemconfig(current_text, text=learning_word, fill=LEARNING_LANG_TEXT_COLOR)
    canvas.itemconfig(card_image, image=card_front_img)
    # wait 3 seconds then flip
    window.after(TIMER, func=flip_card, )
    return


# ---------------------------- UI SETUP ------------------------------- #

current_card = {}

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
card_back_img = PhotoImage(file=CARD_BACK_FILE)
card_image = canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=card_front_img,)

# text on cards
language_text = canvas.create_text([WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5], text="", font=LANGUAGE_FONT,
                                   fill=LEARNING_LANG_TEXT_COLOR)
current_text = canvas.create_text([WINDOW_WIDTH/2, WINDOW_HEIGHT/2], text="", font=WORD_FONT,
                                  fill=LEARNING_LANG_TEXT_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


window.after(3000, func=flip_card,)

# BUTTONS
correct_button = Button(text="✔", background=CORRECT_BG_COLOR, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                        fg=BUTTON_TEXT_COLOR, font=BUTTON_FONT, command=change_word)
correct_button.grid(column=BUTTON_COLUMN_START, row=BUTTON_ROW_START, )

incorrect_button = Button(text="❌", background=INCORRECT_BG_COLOR, fg=BUTTON_TEXT_COLOR, font=BUTTON_FONT,
                          height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=change_word)
incorrect_button.grid(column=BUTTON_COLUMN_START+1, row=BUTTON_ROW_START, pady=BUTTON_PAD_Y,
                      padx=BUTTON_PAD_X,)

change_word()

window.mainloop()


