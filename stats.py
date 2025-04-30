def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    