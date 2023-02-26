def pair_sum(lst, k):
    len_lst = len(lst)

    if len_lst < 2:
        return 0

    seen = set()
    output = set()

    for ind, num in enumerate(lst):
        target = k - num
        if target > 0 and target not in seen:
            seen.add(target)
            try:
                output.add((min(target, num), max(target, num)))
            except ValueError:
                continue

    print("\n".join(map(str, output)))
    return len(output)


print(pair_sum([1, 3, 2, 5, 6], 4))
