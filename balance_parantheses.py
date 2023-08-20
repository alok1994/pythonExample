'''def balancepar(expr):
    openp = set('{[(')
    match = set([('(', ')'), ('{', '}'), ('[',']')])
    stack = []
    if len(expr)%2 != 0:
        return False
    for char in expr:
        if char in openp:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            lastchar = stack.pop()
            
            if (lastchar, char) not in match:
                return False
            
    return len(stack) == 0

print(balancepar('({[]})'))'''

def balance(exp):
    openp = set('({[')
    match = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    if len(exp) % 2 != 0:
        return False
    for char in exp:
        if char in openp:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastchar = stack.pop()
            if (lastchar, char) not in match:
                return False
    return len(stack) == 0

print(balance('{[]}'))
