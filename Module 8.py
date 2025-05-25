import re

"""Asks the user for a filename with the prompt "Please enter filename: "
Tries to open the named file.
If the file fails to open (e.g. because the filename is invalid), the program
should catch the exception, print the message "The file {filename} was not
found." where {filename} is the filename from step 1, and skip the remaining
steps."""


def get_input():
    """getting filename"""
    filename = input("Please enter filename: ")
    try:
        file = open(filename)
        contents = file.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    return re.findall('[a-zA-Z]+', contents)


def extraction(contents):
    """Extraction"""
    length_word = {}
    words = re.findall('[a-zA-Z]+', contents)
    for word in words:
        word = word.lower()
        length = len(word)
        if length in length_word:
            length_word[length].append(word)
        else:
            length_word[length] = [word]
    return length_word


def add_word(word_dict, word):
    """f"""
    length = len(word)
    word_dict.setdefault(length, set()).add(word.lower())


def make_dic(words):
    """f"""
    length_word = {}
    for word in words:
        add_word(length_word, word)
    return length_word


def word_length():
    """f"""
    answer = input("Please enter desired length or 'q' to quit: ")
    if answer == "q":
        return 'q'
    try:
        return int(answer)
    except ValueError:
        print(f"Invalid word length: {answer}")
        return None

def printing(word_dict, length):
    """f"""
    words = word_dict.get(length)
    if not words:
        print(f"There are no words of length {length} in the file.")
        return
    print(f"Words of length {length}:")
    for word in sorted(words):
        print(f"    {word}")







def main():
    """f"""
    words = get_input()
    if words is None:
        return
    word_dict = make_dic(words)
    while True:
        result = word_length()
        if result == 'q':
            break
        if isinstance(result, int):
            printing(word_dict, result)

main()

f

