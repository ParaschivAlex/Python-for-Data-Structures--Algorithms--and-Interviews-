def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output


print(word_split('themanran', ['the', 'ran', 'man']))
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print(word_split('themanran', ['clown', 'ran', 'man']))
