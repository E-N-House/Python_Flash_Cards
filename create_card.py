import random
from create_library import data

user_words = data
def choose_learning_word():
    print("word is chosen")
    random_word = user_words[random.randint(0, len(user_words)-1)]["French"]
    return random_word

