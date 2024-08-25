def main():
    text = get_text()
    words = word_count(text)
    chars_dict = character_dict(text)
    alpha_dict = is_alpha(chars_dict)
    list = chars_list(alpha_dict)
    print("----- Begin report of book 'frankenstein' -----")
    print(f"{words} words found in the document")
    print(list)
    print("----- End report -----")


def word_count(text):
    words = len(text.split())
    return words


def character_dict(text):
    character = {}
    for c in text.lower():
        if c in character:
            character[c] += 1
        else:
            character[c] = 1
    return character


def is_alpha(chars_dict):
    alpha_chars = {}
    for char in chars_dict:
        if char.isalpha():
            count = chars_dict[char]
            alpha_chars[char] = count
    
    return alpha_chars


def chars_list(alpha_dict):
    #alpha_chars = is_alpha()
    new_list = [{key:value} for key, value in alpha_dict.items()]
    return new_list



def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


main()
