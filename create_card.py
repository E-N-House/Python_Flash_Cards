import random
from create_library import data

user_words = data

def choose_learning_card():
    print("word is chosen")
    random_card = random.choice(user_words)
    return random_card

