class Solution:
    def myAtoi(self, st):
        st = st.strip()

        if not st:
            return 0
        negative = False
        out = 0
        if st[0] == '-':
            negative = True
        elif st[0] == '+':
            negative = False
        elif not st[0].isnumeric():
            return 0
        else:
            out = ord(st[0]) - ord('0')
        for i in range(1, len(st)):
             if st[i].isnumeric():
                 out = out*10 + (ord(st[i]) - ord('0'))
                 if not negative and out >= 2147483647:
                    return 2147483647
                 if negative and out >= 2147483647:
                    return -2147483647

             else:
                break
        if not negative:
            return out
        else:
            return -out
s = Solution()
print(s.myAtoi('4322'))
