import sys
from stats import *


def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


def generate_report(text, chars: dict):
    # Sort chars dict in descending by key
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    
    # Print the report
    print(f'----------- Word Count ----------\n' +
            f'Found {count_words(text)} total words\n' +
            '--------- Character Count -------')
    for char, count in sorted_chars.items():
        if char.isalpha() and char != ' ':
            print(f'{char}: {count}')
    print('============= END ===============')


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(f'./{sys.argv[1]}')
    chars = count_characters(text)

    generate_report(text, chars)

if __name__ == "__main__":
    main()
