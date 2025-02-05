def check_that_a_letter_is_in_a_word(word, letter, convergences=""):    
    count = 0
    while True is True:
        if len(word) > count:
            if letter == word[count]:
                convergences = convergences + (letter)
            
            else:
                convergences = convergences + ("_")

            count += 1
        else:
            break
    
    return convergences