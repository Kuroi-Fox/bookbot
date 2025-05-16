from stats import word_count, letter_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = (get_book_text(book).lower())
    num_words = word_count(text)
    char_count = letter_count(text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in char_count:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]
    main()

