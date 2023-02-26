def anagram(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    s1, s2 = s1.replace(" ", ""), s2.replace(" ", "")
    print(s1, s2)
    # Sol 1: Sortare
    # s1 = ''.join(sorted(s1))
    # s2 = ''.join(sorted(s2))
    # if s1 == s2:
    #     return True
    # return False

    # sau return sorted(s1) == sorted(s2)

    # Sol 2: freq. list
    # f1, f2 = [0] * 32, [0] * 32
    # for ch in s1:
    #     f1[ord(ch) - ord('a')] += 1
    # for ch in s2:
    #     f2[ord(ch) - ord('a')] += 1
    # for i in range(32):
    #     if f1[i] != f2[i]:
    #         return False
    # return True

    # Sol 3: 2 dictionaries
    # d = {}
    # dd = {}
    # for ch in s1:
    #     if ch in d:
    #         d[ch]+=1
    #     else:
    #         d[ch] = 1
    # for ch in s2:
    #     if ch in dd:
    #         dd[ch] += 1
    #     else:
    #         dd[ch] = 1
    # return d == dd

    # Sol 4: 1 dictionary
    d = {}
    for ch in s1:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for ch in s2:
        if ch in d:
            d[ch] -= 1
        else:
            d[ch] = 1

    for ch in d:
        if d[ch] != 0:
            return False
    return True


print(anagram('Dog', 'God'))
print(anagram('aa', 'bb'))
print(anagram('abc def', 'adecb f'))
