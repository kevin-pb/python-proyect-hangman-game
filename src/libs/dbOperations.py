def read_db_and_convert_to_list(direction="db\word_list.txt"):
    word_list = open(direction, "r")
    word_list_read = word_list.read()
    word_list_read = word_list_read.split(" ")
    word_list.close
    return word_list_read

def read_db(direction="db\word_list.txt"):
    word_list = open(direction, "r")
    word_list_read = word_list.read()
    word_list.close
    return word_list_read

def db_agregate_one_word(word_to_agregate, direction="db\word_list.txt"):
    word_list = open(direction, "a+")
    word_list.write(f"{word_list.read()} {word_to_agregate}")
    word_list.close
    
