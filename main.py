def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    print(book_content)

if __name__ == "__main__":
    main()
