import random
import re

def checking_concordances(letter, word, empty_list):
    if re.search(f"{letter}+",word):
        for i,e in enumerate(word):
            if e == letter:
                empty_list[int(i)] = e
    else:    
        return False

def convert_list_to_str(object_to_convert):
    object_in_str = ""
    for i in object_to_convert:
        object_in_str += i
    return object_in_str

word_list = ["apple","hello","fire","determination","one","definition","nothing","existence","two"]
random_word = random.choice(word_list)
print(random_word)
list_syllables_random_word = list(random_word)

list_syllables_quantity_random_word = []
for i in list_syllables_random_word:
    list_syllables_quantity_random_word.append("_")
    
print("===The Hangman Game==")
attemps = 3
while list_syllables_quantity_random_word != list_syllables_random_word:
    print(f"You have {attemps} attemps")
    print(f"The word is {convert_list_to_str(list_syllables_quantity_random_word)}")
    data_enter = input("Introduce a letter that you thing that is in the word - ")
    tmp = checking_concordances(data_enter, random_word, list_syllables_quantity_random_word)
    
    if tmp == False:
        attemps -= 1
        if attemps != 0:
            print("You fail")
        if attemps == 0:
            print("You lose!!!")
            break

if list_syllables_quantity_random_word == list_syllables_random_word:
    print(f"You win, the word is {convert_list_to_str(list_syllables_quantity_random_word)}!!!!!!")
