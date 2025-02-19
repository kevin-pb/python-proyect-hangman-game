import random
from libs.checkingModule import checking_concordances as ch_c
from libs.convertListToStrModule import convert_list_to_str as l_to_s

word_list = ["apple","hello","fire","determination","one","definition","nothing","existence","two"]
random_word = random.choice(word_list)

list_syllables_random_word = list(random_word)

list_syllables_quantity_random_word = []
for i in list_syllables_random_word:
    list_syllables_quantity_random_word.append("_")
    
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
    

