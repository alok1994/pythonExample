class Solution:
    def reorderLogFiles(self, logs):
        res1, res2 = [], []

        for log in logs:
            if (log.split()[1].isdigit()):
                res2.append(log)
            else:
                res1.append(log.split())
        print(res1)
        #print(res2)
        res1.sort(key = lambda x: x[0])
        res1.sort(key = lambda x: x[1:])
        print(res1)

        for i in range(len(res1)):
            res1[i] = (' '.join(res1[i]))
        res1.extend(res2)
        print(res1)

logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit log', 'let3 art zero']
s = Solution()
s.reorderLogFiles(logs)
