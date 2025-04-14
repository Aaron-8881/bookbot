import sys

from stats import count_words, count_character, sort_character

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
       
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    character_count = count_character(book_content)
    sorted_chars = sort_character(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
