import random
from lib.check_fns import check_that_a_letter_is_in_a_word as check_l_in_w
from lib.data_enter import ui_interface

word_list = ["apple","hello","fire","determination","one","definition","nothing","existence","two"]
random_word = random.choice(word_list)


chances = 3
coincidences = ""

data_enter = ui_interface()
a=check_l_in_w("determination", data_enter, coincidences)
count = 0

