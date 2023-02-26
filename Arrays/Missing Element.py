def finder(s1, s2):
    # t1, t2 = 0, 0
    # for num in s1:
    #     t1 += num
    # for num in s2:
    #     t2 += num
    # return abs(t1 - t2)
    # sau cu dictionar de aparitii sau cu sortare binara
    # ultima solutie cu xor

    sol = 0
    for num in s1 + s2:
        sol ^= num
        print(sol)
    print(s1 + s2)
    return sol


print(finder([0, 1, 2, 3, 4, 5, 6, 7], [3, 0, 7, 2, 1, 4, 6]))
