def compress(s):
    lg = len(s)
    if lg == 0:
        return
    count = 1
    sol = ""
    for i in range(1, lg):
        if s[i] != s[i - 1]:
            sol += s[i - count]
            sol += str(count)
            count = 1
        else:
            count += 1
    sol += s[i - count + 1]
    sol += str(count)
    return sol

# sau cu dictionar

print(compress("AAAAABBBBCCCC"))
