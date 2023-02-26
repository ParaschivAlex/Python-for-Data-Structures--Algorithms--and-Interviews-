def reverse(s):
    # if s == '':
        # return ''
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[0:len(s) - 1])
        # return reverse(s[1:]) + s[0]


print(reverse('hello world'))
