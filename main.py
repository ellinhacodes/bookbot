import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
   
    print("----------- Word Count ----------")
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    characters = count_characters(book_text)
    sorted_list = sort_characters(characters)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
