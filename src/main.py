# Importing modules-----------------
from libs.workWithWords import random_word_selector as r_word_selector
from libs.workWithWords import wordSyllablesQuantity
from libs.dbOperations import read_db_and_convert_to_list
from libs.uiInterface import uiInterface
# Importing modules-----------------

random_word = r_word_selector(read_db_and_convert_to_list())
list_syllables_random_word = list(random_word)
list_syllables_quantity_random_word = []

wordSyllablesQuantity(list_syllables_random_word, list_syllables_quantity_random_word)

uiInterface(random_word, list_syllables_random_word, list_syllables_quantity_random_word)
