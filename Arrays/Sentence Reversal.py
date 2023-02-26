def rev_word(s):
    # removes spaces in the string
    stack = s.split()

    # Length of stack without spaces
    length = len(stack)

    # Empty list for reversal
    rev = []

    # Following FILO or LIFO reverses the list
    for n in range(length):
        rev.append(stack.pop())
    print(rev)

    # Prints the list without trailing white space!
    return ' '.join(word for word in rev)
    # return ' '.join(rev)


print(rev_word("Hi John,    are you ready to rumble?"))
print(rev_word("      space before              "))
