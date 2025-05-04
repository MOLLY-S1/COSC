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
        return contents
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None


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


def looping(diction):
    """Loop until fail"""
    answer = input("Please enter desired length or 'q' to quit: ")
    answer = int(answer)
    while answer not in diction.keys() or answer != 'q':
        if str(answer) == "q":
            break
        try:
            answer = int(answer)
            answering = diction[answer]
            answern = sorted(answering)
            print(f"Words of length {answer}:")
            for answers in answern:
                print(f"    {answers}")
        except IndexError:
            answer = int(answer)
            print("There are no words of length {integer} in the file.")
        except ValueError:
            answer = int(answer)
            print("Invalid word length: {string_user_entered}")
        answer = input("Please enter desired length or 'q' to quit: ")








contents = get_input()
diction = extraction(contents)
looping(diction)

