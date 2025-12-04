def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_character_count(text):
    character_count = {}
    lowercase_text = text.lower()

    for character in lowercase_text:
        if character not in character_count:
            character_count[character] = 0
        character_count[character] += 1

    return character_count

def sort_on(items):
    return items["num"]

def get_sorted_dictionary(dictionary):
    character_list = []
    for character in dictionary:
        character_list.append({"char": character, "num": dictionary[character]})

    character_list.sort(reverse=True, key=sort_on)

    return character_list
