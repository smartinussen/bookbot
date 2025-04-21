import sys
from stats import book_word_count, book_character_count, book_report


def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    word_count = book_word_count(get_book_text(sys.argv[1]))
    sorted_list = book_report(book_character_count(get_book_text(sys.argv[1])))
    print(f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------''')
    print(f"Found {word_count} total words")
    # book_character_count(get_book_text("books/frankenstein.txt"))
    print("--------- Character Count -------")

    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")



main()