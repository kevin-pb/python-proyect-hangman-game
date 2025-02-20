from libs.workWithWords import checking_concordances as ch_c
from libs.workWithWords import convert_list_to_str as l_to_s
from libs.dbOperations import read_db
from libs.dbOperations import db_agregate_one_word

def uiInterface(word, list_syllables, empty_list, cuonter = 3):

    print("===The Hangman Game==\n")
    print("1-Play")
    print("2-Agregate a word to the options")
    print("3-See the options")
    print("4-Exit")  
    while True is True:
        try:
            option = int(input("Introduce the number of one option: "))
        except ValueError:
            print("Incorrect opton")
            option = int(input("Introduce the number of one option: "))
        if option == 1:
            while empty_list != list_syllables:
                print(f"You have {cuonter} attemps")
                print(f"The word is {l_to_s(empty_list)}")
                data_enter = input("Introduce a letter that you thing that is in the word - ")
                tmp = ch_c(data_enter, word, empty_list)

                if tmp == False:
                    cuonter -= 1
                    if cuonter != 0:
                        print("You fail")
                    if cuonter == 0:
                        print("You lose!!!")
                        break
                elif empty_list == list_syllables:
                    print(f"You win, the word is {l_to_s(empty_list)}!!!!!!")

        elif option == 2:
            db_agregate_one_word(input("Introduce a new word: "))
        

        elif option == 3:
            print(read_db())

        elif option == 4:
            break
        
        else:
            print("Incorrect opton")