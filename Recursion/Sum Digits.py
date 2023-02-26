def sum_func(n):
    if n // 10 == 0:
        # print(n)
        return n
    else:
        # print(n)
        return n % 10 + sum_func(n // 10)


print(sum_func(4321))
