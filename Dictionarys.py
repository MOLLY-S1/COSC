def create_index(words_on_page):
    """takes a dictionary mapping from page number to a list of the unique words
    on that page and returns a dictionary that maps from a word to an ordered
    list of pages on which that word appears."""
    new = {}
    for page, words in words_on_page.items():
        for word in words:
            if word not in new:
                new[word] = [page]
            else:
                new[word].append(page)
    return new


input_dict = {
   1: ['hi', 'there', 'fred'],
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']
}
output_dict = create_index(input_dict)
for word in sorted(output_dict.keys()):
    print(f"{word}: {output_dict[word]}")