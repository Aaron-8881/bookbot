def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
