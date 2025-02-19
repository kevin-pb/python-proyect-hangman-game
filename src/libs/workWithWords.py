import re
import random

def checking_concordances(letter, word, empty_list):
    if re.search(f"{letter}+",word):
        for i,e in enumerate(word):
            if e == letter:
                empty_list[int(i)] = e
    else:    
        return False
    
def wordSyllablesQuantity(list_syllables, emptylist):
    for i in list_syllables:
        emptylist.append("_")

def random_word_selector(words_list):
    random_word = random.choice(words_list)
    return random_word

def convert_list_to_str(object_to_convert):
    object_in_str = ""
    for i in object_to_convert:
        object_in_str += i
    return object_in_str