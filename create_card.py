import random

test_list = [{"english": "hello", "french": "bonjour"}, {"english": "goodbye", "french": "aurevoir"}]

def choose_learning_word():
    print("word is chosen")
    random_word = test_list[random.randint(0, len(test_list)-1)]["french"]
    return random_word

