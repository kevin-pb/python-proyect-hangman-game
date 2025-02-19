def db_agregate_one_word(word_to_agregate):
    word_list = open("db\word_list.txt", "a")
    print(word_list.write(f"{word_list.read()} {word_to_agregate}"))
