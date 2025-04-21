def book_word_count(text):
    num_words = len(text.split())
    # print(f"{num_words} words found in the document")
    return num_words
def book_character_count(text):
    characters_dict = {}
    for character in text:
        if character.lower() in characters_dict:
            characters_dict[character.lower()] += 1
        else:
            characters_dict[character.lower()] = 1
    return characters_dict

def sort_on(dict):
    return dict["count"]

def book_report(characters_dict):
    sorted_list = []
    # Iterate through the dictionary
    for char, count in characters_dict.items():
        char_dict = {"char": char, "count": count}
        # Add it to our list
        sorted_list.append(char_dict)
        sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list