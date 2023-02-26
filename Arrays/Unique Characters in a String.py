def uni_char(s):
    # dictionar sau set cu verificare de len sau set cu adaugare de elemente si verificare daca a fost deja adaugat
    # ss = set(s)
    # return len(ss) == len(s)
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            return False
    return True
    # a treia solutie are aceeasi complexitate timp (a doua sol e cea mai slaba dar tot buna)


print(uni_char("aabcd"))
print(uni_char("abcde"))
