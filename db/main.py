# Importing modules-----------------
from libs.checkingModule import checking_concordances as ch_c
from libs.convertListToStrModule import convert_list_to_str as l_to_s
from libs.randomWordSelectorModule import random_word_selector as r_word_selector
from libs.wordSyllablesQuantityModule import wordSyllablesQuantity
# Importing modules-----------------

random_word = r_word_selector(["apple","hello","fire","determination","one","definition","nothing","existence","two"])
list_syllables_random_word = list(random_word)
list_syllables_quantity_random_word = []

wordSyllablesQuantity(list_syllables_random_word, list_syllables_quantity_random_word)

print("===The Hangman Game==")
attemps = 3
while list_syllables_quantity_random_word != list_syllables_random_word:
    print(f"You have {attemps} attemps")
    print(f"The word is {l_to_s(list_syllables_quantity_random_word)}")
    data_enter = input("Introduce a letter that you thing that is in the word - ")
    tmp = ch_c(data_enter, random_word, list_syllables_quantity_random_word)
    
    if tmp == False:
        attemps -= 1
        if attemps != 0:
            print("You fail")
        if attemps == 0:
            print("You lose!!!")
            break

if list_syllables_quantity_random_word == list_syllables_random_word:
    print(f"You win, the word is {l_to_s(list_syllables_quantity_random_word)}!!!!!!")
