import random
from create_library import learning_data

# user_words = learning_data


def choose_learning_card():
    # print("word is chosen")
    random_card = random.choice(learning_data)
    return random_card

