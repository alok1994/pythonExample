def solve(str1):
   res = ""
   cnt = 1
   for i in range(1, len(str1)):
      #import pdb;pdb.set_trace()
      if str1[i - 1] == str1[i]:
         cnt += 1
      else:
         if cnt > 1:
            res += str(cnt)
         res = res + str1[i -1]
         cnt = 1
   if cnt > 1:
        res += str(cnt)
   res = res + str1[-1]
   return res

s = "ABBCCCDEEEEA"
print(solve(s))
