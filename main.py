def main():
    text = get_text()
    num_words = get_word_count(text)
    chars_dict = get_character_dict(text)
    sorted_list = dict_to_sorted_list(chars_dict)

    
    print("----- Begin report of book 'frankenstein' -----")
    print(f"{num_words} words found in the document")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("----- End report -----")


def is_alpha(chars_dict):
    alpha_chars = {}
    for char in chars_dict:
        if char.isalpha():
            count = chars_dict[char]
            alpha_chars[char] = count
    
    return alpha_chars


def dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(dict):
    return dict["num"]


def get_character_dict(text):
    character = {}
    for c in text.lower():
        if c in character:
            character[c] += 1
        else:
            character[c] = 1
    return character


def get_word_count(text):
    return len(text.split())


def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


main()
