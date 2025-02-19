import re

def checking_concordances(letter, word, empty_list):
    if re.search(f"{letter}+",word):
        for i,e in enumerate(word):
            if e == letter:
                empty_list[int(i)] = e
    else:    
        return False