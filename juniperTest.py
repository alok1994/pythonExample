def order(num):
    ords = 0
    while num != 0:
        ords += 1
        num = num // 10
    return ords

def armStrongNumber(num):
    ords = order(num)
    temp = num
    sums = 0
    while num != 0:
        r = num % 10
        sums = sums + r ** ords
        num = num // 10

    if temp == sums:
        print('Number is armstrong number')
    else:
        print('Number is not armstrong number')


armStrongNumber(1634)



def balancePar(strs):
    openP = set('[{(')
    matchP = set([('(', ')'), ('{', '}'), ('[', ']')])
    stack = []
    if len(strs) % 2 != 0:
        return False
    for i in strs:
        if i in openP:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            lastS = stack.pop()
            if ( lastS, i) not in matchP:
                return False
    return len(stack) == 0
print(balancePar('[{}]'))

sts = 'Hello World'
d = {}
for  i in sts:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1


print(d)



class A:
    def __init__(self, firstName):
        self.firstName = firstName

    def printFirstName(self):
        print('First Name:', self.firstName)

class B(A):
    def __init__(self, middleName, firstName):
        self.middleName = middleName
        A.__init__(self, firstName)

    def printMiddleName(self):
        print('Middle Name: ', self.middleName)
        
class C(B,A):
    def __init__(self, lastName, middleName, firstName):
        self.lastName= lastName
        B.__init__(self, middleName, firstName)

    def printFullName(self):
        print('Full Name: ', self.firstName, self.middleName, self.lastName)

obj = C('Verma', 'Kumar', 'Alok')
obj.printFullName()

def compress(s):
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result = result + s[i-1]
            count = 1
    if count > 1:
        result += str(count)
    result = result + s[-1]
    
    return result
    

s = "ABBCCCDEEEEA"
print(compress(s))

def smartDivide(func):
    def inner(a,b):
        print('Dividing a via b')
        if b == 0:
            print('Can not divide via zeor')
            return
        func(a,b)
    return inner
        

@smartDivide
def divide(a,b):
    print(a/b)

divide(4,2)




def feb(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+ b

for i in feb(5):
    print(i, end= ' ')

print('\n')

l1 = [[1,2], [3,4], [5,6], [7,8]]
l2 = [[9,10], [11,12], [13,14],[15,16]]

# l3 = [[10,12],[14,16], [18, 20], [22, 24]]
l3 = []
for value1, value2 in zip(l1,l2):
   # print(value1, value2)
    l4 = []
    for value3 in range(len(value1)):
        sumn = value1[value3] + value2[value3]
        l4.append(sumn)
    l3.append(l4)

#print(l1)
#print(l2)
print(l3)

def longestCommom(text1, text2):
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
print(longestCommom(text1, text2))



'''import requests

import json


header = {'Contect-Type': 'application/json', 'Accept': 'application/json'}
responseData = requests.get('https://jsonplaceholder.typicode.com/users', headers= header)
if responseData.status_code == 200:
    print(responseData.status_code)
    print(json.loads(responseData.content))'''

rows = 5
b = 0
for i in range(rows, 0, -1):
    b = b + 1
    for j in range(1,i+1):
        print(b,end=' ')
    print(' ')


'''rows = int(input("Enter the number:"))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print(' ')'''


rows = 5
for i in range(rows+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print('\n')


ls = [1,2,3,4,5,6,7,8,9]
new = []
for i in range(len(ls)-2):
    temp = []
    for j in range(i, i+3):
        temp.append(ls[j])
    new.append(temp)

print(new)


start = 0
new1 = []
while start < len(ls):
    temp = []
    for j in range(start, start + 3):
        temp.append(ls[j])
    start = start + 3
    new1.append(temp)
print(new1)



rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i,end=' ')
    print(' ')


rows =  6

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(rows, end=' ')
    print(' ')

rows = 6
space= rows
for i in range(1,rows):
    for sp in range(1, space):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print(' ')
    space = space - 1


ls = list(range(2,100))
#print(ls)
prim = []
for i in ls:
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        prim.append(i)
print(prim)





print('__name__', __name__)
if __name__ == '__main__':
    print('Executing directly')




def romanInt(sts):
    total = 0
    curr = 0
    prev = 0
    dictR = {'I': 1, 'V': 5, 'C': 100, 'L': 50}
    for i in sts:
        curr = dictR[i]
        if curr > prev :
            total = total + curr - 2 * prev
        else:
            total += curr
        prev = curr

    return total
print(romanInt('IV'))


def argsKeyargs(arg, *args,**kargs):
    print('arg:',arg)
    print(args)
    print(kargs['first'])

argsKeyargs(1, 'alok', 'kumar', first='alok', surname='verma' )


def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} via {} '.format(a,b))
        if b == 0:
            print('Can not divide any number via zero')
            return
        return func(a,b)
    return inner

@smartDivide
def divide(a,b):
    print(a/b)
#
divide(4,2)
#a = 4
#b = 2
#new = smartDivide(divide(a,b))
#new(a,b)


def longestSubString(sts):
    if len(sts) == 0:
        return 0
    d = {}
    maxL = 0
    start = 0
    for i in range(len(sts)):
        if sts[i] in d:
            start = d[sts[i]] + 1
        else:
            maxL = max(maxL , i - start + 1)
        d[sts[i]] = i
    return maxL

print(longestSubString('abcdaefg'))

def subArray(arr):
    maxS = maxT = arr[0]
    for i in arr[1:]:
        maxT = max(maxT+i, i)
        maxS = max(maxT, maxS)
    return maxS

inputs = [-2,1,-3,4,-1,2,1,-5,4]
#output: 6
print(subArray(inputs))

def sumTwoNumbers(arr, target):
    result = set()
    arr.sort()
    for i in range(len(arr)):
        left = i
        right = len(arr) - 1
        while left < right:
            sm = arr[left] + arr[right]
            if sm == target:
                result.add((arr[left], arr[right]))
            if sm < target:
                left += 1
            else:
                right -= 1
    return result
    


ls = [1,3,0,8,7,4,2,5,6]
target = 7
print(sumTwoNumbers(ls, target))


l1 = [5,2,1,0,19,32,22,20,23]
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i] < l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
print(l1)

l4 = [5,2,1,0,19,32,22,20,23]
fmax = l4[0]
smax = l4[0]

for i in range(len(l4)):
    if l4[i] > fmax :
        smax = fmax
        fmax = l4[i]
    elif l4[i] > smax:
        smax = l4[i]
print(smax)



l5 = [5,2,1,0,19,32,22,20,23]
fmax = l5[0]
smax = l5[0]
tmax = l5[0]
for i in range(len(l5)):
    if l5[i] > fmax:
        tmax = smax
        smax = fmax
        fmax = l5[i]
    elif l5[i] > smax:
        tmax = smax
        smax = l5[i]
    elif l5[i] > tmax:
        tmax = l5[i]

print(tmax)



def reverseNum(num):
    res = 0
    while num > 0:
        remain = num % 10
        res = res  * 10 + remain
        num = num // 10
    return res
print(reverseNum(1234))


def subArray(nums, target):
    d = {0:1}
    s = 0
    count = 0
    for i in nums:
        s += i
        if s - target in d:
            count += d[s - target]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return count

nums = [3,4,7,2,-3,1,4,2,1]
target = 7
print(subArray(nums, target))

def QuadSum(arr, target):
    res = set()
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            left = j + 1
            right = len(arr) -1
            while left < right:
                s = arr[i] + arr[j] + arr[left]+ arr[right]
                if s == target:
                    res.add((arr[i], arr[j], arr[left], arr[right]))
                if s < target:
                    left += 1
                else:
                    right -= 1
    return res

arr = [-1,0,-2,-1,2]
target = 0
print(QuadSum(arr, target))

def threeSumClosest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) -1
        while left < right:
            sumhere = nums[i] + nums[left] + nums[right]
            if abs(sumhere - target) < abs( res - target):
                res = sumhere
            if sumhere < target:
                left += 1
            else:
                right -= 1
    return res
nums =[-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))



def customList(nums):
    curr = [nums[0]]
    res = []
    for i in nums[1:]:
        if (i - 1) != curr[-1]:
            res.append(curr)
            curr = [i]
        else:
            curr.append(i)
    res.append(curr)
    return res

ls = [1,2,3,4,7,8,9,11,23,24, 26]
print(customList(ls))
