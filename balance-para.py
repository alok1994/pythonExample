class Solution:
    def balancePar(self, expr):
        openex = set('([{')
        match = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        if len(expr) % 2 != 0 :
            return False
        for i in expr:
            if i in openex:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if (last, i) not in match:
                    return False
        return len(stack) == 0
    

s = Solution()
print(s.balancePar('{[]}'))
