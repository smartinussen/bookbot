from stats import book_word_count, book_character_count, book_report

def get_book_text(path):
    with open(path) as book:
        text = book.read()
    return text

def main():
    # get_book_text("books/frankenstein.txt")
    word_count = book_word_count(get_book_text("books/frankenstein.txt"))
    sorted_list = book_report(book_character_count(get_book_text("books/frankenstein.txt")))
    print('''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
    print(f"{word_count} words found in the document")
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