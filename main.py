def main():
    text = get_text()
    print(word_count(text))
    print(character_count(text))


def word_count(text):
    words = len(text.split())
    return words


def character_count(text):
    character = {}
    for c in text.lower():
        if c in character:
            character[c] += 1
        else:
            character[c] = 1
    return character


def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


main()
