# this is my attempt at creating code that fulfills the assignment with some help from chatGPT
# and the answer key. 
def main():
    filename = "Frankenstein"
    book = get_book(filename)
    word_count = count_words(book)
    letter_count = create_letter_count(book)
    letter_count_sorted = sort_dict(letter_count)
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()

    for key, value in letter_count_sorted.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

# takes the filename, (which for this exercise is always Frankenstein) and returns a string
# of the file's contents
def get_book(filename):
    with (open(f"books/{filename}.txt")) as f:
        return f.read()

# takes a string and returns how many words are in it
def count_words(book):
    split_book = book.split()
    num_words = len(split_book)
    return num_words

# takes a dictionary of string : int and sorts it based on the value of the int descending
def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse = True))

# takes a string, makes it lower case, uses a dictionary of string : int to count how many
# times a letter comes up
def create_letter_count(book):
    book_lower = book.lower()
    letter_count = {}
    for letter in book_lower:
        if not letter.isalpha():
            pass
        elif letter not in letter_count:
            letter_count[letter] = 1
        else: 
            letter_count[letter] += 1
    return letter_count

main()
