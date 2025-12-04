import sys
from stats import get_num_words, get_character_count, get_sorted_dictionary

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    words_total = get_num_words(book_text)
    character_totals = get_character_count(book_text)
    character_dict = get_sorted_dictionary(character_totals)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words_total} total words")
    print("--------- Character Count -------")
    for item in character_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
