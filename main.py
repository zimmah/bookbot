def main():
    books = ["frankenstein"]
    frankenstein = get_book_text(books[0])
    number_of_words = get_number_of_words(frankenstein)
    count_of_characters = get_count_of_characters(frankenstein)
    print(f"{books[0]} has {number_of_words} words.")
    print(count_of_characters)

def get_book_text(title):
    books_path = "books/"
    with open(f"{books_path}{title}.txt") as book:
        return book.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_count_of_characters(text):
    lowercase_text = text.lower()
    count_of_characters = {}
    for character in lowercase_text:
        if character in count_of_characters:
            count_of_characters[character] += 1
        else:
            count_of_characters[character] = 1
    return count_of_characters
    
main()