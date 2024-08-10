def main():
    titles = ["frankenstein"]
    pretty_print_report(titles[0])

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
        if not character.isalpha():
            continue
        if character in count_of_characters:
            count_of_characters[character] += 1
        else:
            count_of_characters[character] = 1
    return count_of_characters

def format_dictionary(dictionary):
    list_of_dictionaries = []
    for character in dictionary:
        list_of_dictionaries.append({"character": character, "count": dictionary[character]})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

def sort_on(dictionary):
    return dictionary["count"]

def pretty_print_report(title):
    text = get_book_text(title)
    sorted_list_of_character_counts = format_dictionary(get_count_of_characters(text))
    print(f"--- Begin report of {title} ---")
    print(f"{get_number_of_words(text)} words found in the document")
    print("")
    for character_count in sorted_list_of_character_counts:
        print(f"the {character_count['character']} character was found {character_count['count']} times")
    print("--- End report ---")

main()