def censor_digits(string):
    """takes a string and returns a new string where all digit characters are
    replaced with an asterisk character, '*'."""
    wordy = []
    for c in string:
        if str.isdigit(c):
            c = "*"
            wordy.append(c)

        else:
            wordy.append(c)
    letter = "".join(wordy)
    return letter


print(censor_digits("Angus McGurkinshaw: 2000.0 Suzan Buckingdale: 2500.0 Suzan McGurkinshaw: 2000.0"))
