# this is my attempt at creating code that fulfills the assignment with some help from chatGPT
# and the answer key. I should redo this and define more functions with individual functions
# instead of having a ton of stuff bundled into like 2 functions
# also I should find a more eloquent way to create a dictionary instead of brute forcing it.
def main():
    filename = "Frankenstein"
    word_count = count_words(filename)
    letter_count = read_book(filename)
    letter_count_sorted = sort_dict(letter_count)
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()

    for key, value in letter_count_sorted.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


def count_words(filename):
     with open(f"books/{filename}.txt") as f:
        file_contents = f.read()
        split_book = file_contents.split()
        num_words = len(split_book)
        return num_words
     
def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse = True))

def read_book(filename):
    with open(f"books/{filename}.txt") as f:
        file_contents = f.read()
        split_book = file_contents.split()
        num_words = len(split_book)
        file_lower = file_contents.lower()
        letter_count = {'a': 0,
                        'b': 0,
                        'c': 0,
                        'd': 0,
                        'e': 0,
                        'f': 0,
                        'g': 0,
                        'h': 0,
                        'i': 0,
                        'j': 0,
                        'k': 0,
                        'l': 0,
                        'm': 0,
                        'n': 0,
                        'o': 0,
                        'p': 0,
                        'q': 0,
                        'r': 0,
                        's': 0,
                        't': 0,
                        'u': 0,
                        'v': 0,
                        'w': 0,
                        'x': 0,
                        'y': 0,
                        'z': 0}
        for letter in file_lower:
            for key in letter_count:
                if letter == key:
                    letter_count[key] += 1
        return letter_count

main()
