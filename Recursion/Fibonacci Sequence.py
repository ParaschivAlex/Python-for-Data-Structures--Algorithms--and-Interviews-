# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] is not None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


def fib_iter(n):
    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):
        print(a, b)
        a, b = b, a + b

    return a


def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_rec(10))
print(fib_dyn(10))
print(fib_iter(10))
