from Stack import Stack


def check(string):
    if len(string) % 2 != 0:
        return False
    opening = set('([{')
    matches = [('(', ')'), ('[', ']'), ('{', '}')]
    stack = Stack()
    for ch in string:
        if ch in opening:
            stack.push(ch)
        else:
            if len(stack.stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, ch) not in matches:
                return False
    return len(stack.stack) == 0


print(check('[]'))
print(check('()[]{}((()))[]'))
print(check('(({[['))
print(check('([())]'))
print(check(''))
