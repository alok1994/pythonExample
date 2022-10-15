def argskeyargs(arg, *args, **kwargs):
    print('First Arg', arg)
    print('Args', args)
    print('keyword args', kwargs)

argskeyargs(1,232,22,first='alok', second='kumar')



def balanceParan(strs):
    stack = []
    openp = set('{[(')
    match = set([('(',')'), ('[', ']'), ('{', '}')])
    if len(strs) %2 != 0:
        return False
    for i in strs:
        if i in openp:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (last, i) not in match:
                return False
    return len(stack) == 0

print(balanceParan('({[][})]'))




class A:
    def __init__(self, firstName):
        self.firstName = firstName

    def printFirstName(self):
        print('First Name', self.firstName)

class B(A):
    def __init__(self, middleName, firstName):
        self.middleName = middleName
        A.__init__(self,firstName)

    def printMiddleName(self):
        print('Middle Name', self.middleName)

class C(B):
    def __init__(self,lastName, middleName, firstName):
        self.lastName = lastName
        B.__init__(self,middleName, firstName)

    def printFullName(self):
        print('Full Name:', self.firstName, self.middleName, self.lastName)


obj = C('Verma', 'Kumar', 'Alok')
obj.printFullName()



def compress(str1):
    count = 1
    res = ''
    for i in range(1, len(str1)):
        if str1[i-1] == str1[i]:
            count += 1
        else:
            if count > 1:
              res = res + str(count)
            res = res + str1[i-1]
            count = 1
    if count > 1:
        res = res + str(count)
    res = res + str1[-1]
    return res

print(compress('ABBCCCDDDDEA'))
# A2B3C4DEA


def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} via {}'.format(a,b))
        if b == 0:
            print('Ohh! Can not divide via zero')
            return
        return func(a,b)
    return inner

@smartDivide
def dividen(a,b):
    print(a/b)


dividen(4,2)


def longestSubString(str1):
    if len(str1) ==  0:
        return 0
    d = {}
    maxL = 0
    start = 0
    for i in range(len(str1)):
        if str1[i] in d:
            start = d[str1[i]] + 1
        else:
            maxL = max(maxL, i - start + 1)
        d[str1[i]] = i
    return maxL


print(longestSubString('abcdaefg'))


def subArray(arr):
    maxS = maxT = arr[0]
    for i in arr[1:]:
        maxT = max(maxT + i, i)
        maxS = max(maxS, maxT)
    return maxS


inputs = [-2,1,-3,4,-1,2,1,-5,4]
#output: 6
print(subArray(inputs))


def sumTwoNumers(arr, target):
    res = set()
    arr.sort()
    for i in range(len(arr)):
        left = i
        right = len(arr) -1
        while left < right:
            sm = arr[left] + arr[right]
            if sm == target:
                res.add((arr[left], arr[right]))
                left += 1
                right -= 1
            elif sm < target:
                left += 1
            else:
                right -= 1
    return res

ls = [1,3,0,8,7,4,2,5,6]
target = 7
print(sumTwoNumers(ls, target))




l1 = [5,2,1,0,19,32,22,20,23]
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i] < l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print(l1)



l2 = [5,2,1,0,19,32,22,20,23]
l3 = []
i = 0
while i < len(l2):
    mins = l2[i]
    for j in range(len(l2)):
        if mins > l2[j]:
            mins = l2[j]
            
    l3.append(mins)
    l2.remove(mins)
    

print(l3)



l4 = [5,2,1,0,19,32,22,20,23]
fmax = l4[0]
smax = l4[1]
for i in range(len(l4)):
    if l4[i] > fmax:
        smax = fmax
        fmax = l4[i]
    elif l4[i] > smax and l4[i] != fmax:
        smax = l4[i]

print(smax)



l5 = [5,2,1,0,19,32,22,20,23]
fmax = l5[0]
smax = l5[1]
tmax = l5[2]
for i in range(len(l5)):
    if l5[i] > fmax:
        tmax = smax
        smax = fmax
        fmax = l5[i]
    elif l5[i] > smax :
        tmax = smax
        smax = l5[i]
    elif ls[i] > tmax:
        tmax = l5[i]

print(tmax)


ls = list(range(1,100))
ls1 = []
for i in ls[2:]:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        ls1.append(i)
print(ls1)


str1 = 'alok'
print(str1[::-1])

def reverseNumber(num):
    res = 0
    while num > 0:
        remain = num % 10
        res = res * 10 + remain
        num = num // 10
    return res
print(reverseNumber(1234))

def subArray(nums, target):
    sumDict = {0:1}
    s = 0
    count = 0
    for i in nums:
        s += i
        if s - target in sumDict:
            count += sumDict[s - target]
        if s in sumDict:
            sumDict[s] += 1
        else:
            sumDict[s]  = 1
    return count

nums = [3,4,7,2,-3,1,4,2,1]
target = 7
print(subArray(nums, target))


def QuadSum(arr, target):
    res = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            left = j + 1
            right = len(arr) - 1
            while left < right:
                s = arr[left] + arr[right] + arr[i] + arr[j]
                if s == target:
                    res.append((arr[i],arr[j],arr[left],arr[right]))
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return res

arr = [-1,0,-2,-1,2]
target = 0
print(QuadSum(arr, target))

str1 = 'alok kumar verma alok'
d = {}
for i in list(str1):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)


def threeSumClosest(arr, target):
    arr.sort()
    res = sum(arr[:3])
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            sumhere = arr[i] + arr[left] + arr[right]
            if abs(sumhere - target) < abs(res - target):
                res = sumhere
            if sumhere < target:
                left += 1
            else:
                right -= 1
    return res

nums =[-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))

def threeSum(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sumhere = nums[i] + nums[left] + nums[right]
            if sumhere == target:
                res.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sumhere < target:
                left += 1
            else:
                right -=1
    return res


nums = [-1,1,0,2,3, -2]
target = 1
print(threeSum(nums, target))




'''*************
 ***********
  *********
   *******
    *****
     ***
      **
       *
'''

rows = 6
sp = 1
for i in range(rows, 0, -1):
    for k in range(sp):
        print(' ', end = '')
    for j in range(i):
        print('*', end= ' ')
    print(' ')
    sp += 1
    
'''12345
1234
123
12
1'''


for i in range(rows, 0, -1):
    for j in range(1,i):
        print(j, end=' ')
    print(' ')



for i in range(rows+1):
    for j in range(i):
        print('*', end= ' ')
    print(' ')



ls = [0,1,2,3,4,5,6,7,8,9]
ls1 = []
i = 0
j = len(ls) -1
while i < len(ls):
    ls1.append(i)
    ls1.append(j)
    i += 1
    j -= 1
    ls.remove(i)
    
print(ls1)

def romanToInt(str1):
    total = 0
    curr = 0
    prev = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in str1:
        curr = rom[i]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total += curr
        prev = curr

    return total

print(romanToInt('XLIX'))


def orders(nums):
    n = 0
    while nums != 0:
        n = n + 1
        nums = nums // 10
    return n

def armstrong(nums):
    ords = orders(nums)
    s = 0
    temp = nums
    while nums != 0:
        r = nums % 10
        s += r ** ords
        nums = nums // 10
    if s == temp:
        print('Armstrong number')
    else:
        print('Not armstrong number')


armstrong(1634)


str1 = 'my email id is alok.kumar_verma@nokia.com'

import re
email = re.findall(r'\w+[.]\w+[_]\w+[@]\w+[.]\w+', str1)
print(email)


def feb(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = a+b, a

for i in feb(5):
    print(i, end=' ')
print('\n')

def subSequence(text1, text2):
    n,m = len(text1), len(text2)
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
print(subSequence(text1, text2))



rows = 6
b = 0
for i in range(rows, 0, -1):
    b = b + 1
    for j in range(1,i):
        print(b,end=' ')
    print(' ')
