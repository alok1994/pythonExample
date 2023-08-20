def argtest(arg, *args, **kwargs):
    print(arg)
    print(args)
    print(kwargs)

argtest('Alok', 'kumar', 'verma', name= 'alok', surname='verma')


def balancePar(strs):
    stack = []
    openp = set('[{(')
    matchp = set([('(', ')'), ('[', ']'), ('{', '}')])
    for char in strs:
        if char in openp:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if ( last, char) not in matchp:
                return False
    return len(stack) == 0

print(balancePar('([])'))



ls = [2,3, -2, 3,-1,5,6,7,4]
target = 3
#3
#3
#3
#5
#6
#7
for i in range(len(ls) - target):
    subArr = []
    for j in range(i, i + target):
        subArr.append(ls[j])
    print(max(subArr))
    
ls1 = [2,3,5,6,2,2,0,1,2]
ls2 = sorted([ i for i in ls1 if i != 2 ]) + [j for j in ls1 if j == 2]
print(ls2)




class A:
    def __init__(self, firstName):
        self.firstName = firstName

    def printFirstName(self):
        print("First Name:", self.firstName)

class B(A):
    def __init__(self, middleName, firstName):
        self.middleName = middleName
        A.__init__(self, firstName)
        
    def printMiddleName(self):
        print("Middle Name:", self.middleName)

class C(B):
    def __init__(self, lastName, middleName, firstName):
        self.lastName = lastName
        B.__init__(self, middleName, firstName)

    def printFullName(self):
        print("Full Name:", self.firstName, self.middleName, self.lastName)

obj = C('Kumar', 'Verma', 'Alok')
obj.printFullName()



def compress(strs):
    res = ''
    count = 1
    for i in range(1, len(strs)):
        if strs[i - 1] == strs[i]:
            count += 1
        else:
            if count > 1:
                res = res + str(count)
            res = res + strs[i -1]
            count =1
    if count > 1:
        res = res + str(count)
    res = res + strs[-1]
    return res            


strs = 'ABBCCCDDDDAE'
print(compress(strs))



import requests
from requests.auth import HTTPBasicAuth
import json

header = {'Content-Type': 'application/json', 'Accept': 'application/json'}


response = requests.get('https://jsonplaceholder.typicode.com/users', headers = header)
if response.status_code == 200:
    data = json.loads(response.content)
    for  i in data:
        print('Name: {}, \nAddress: {}'.format(i['name'], i['address']))


# Decorate is a inbuild funtion in function which will extend the behaviour of followed function without modifying.

def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} by {}'.format(a,b))
        if b == 0:
            print("Can't divide any number by  zero")
            return
        return func(a,b)
    return inner

@smartDivide
def divide(a,b):
    print(a/b)

divide(4,0)

from datetime import date

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printNameAge(self):
        print("Name: {} and Age: {}".format(self.name, self.age))

    @classmethod
    def ageYear(cls, name, tyear):
        today = date.today()
        return cls(name, today.year - tyear)

obj = A('Alok', 30)
obj.printNameAge()

c = A.ageYear('Advik', 2021)
c.printNameAge()



print("File __name__ is:", __name__)

if __name__ == "__main__":
    print("file directly executed")
    divide(10,2)
else:
    print("file imported and executed")


ls  = [1,2,3,4,5,6,7,8,9,10]
print(list(filter( lambda x: x % 2 == 0, ls)))


print(list(map(lambda x: x *2 , ls)))


def longestCommonPrefix(st):
    minl = len(st[0])
    for i in st[1:]:
        minl = min(minl, len(i))
    lcp = ''
    k = 0
    while k < minl:
        char = st[0][k]
        for j in range(1, len(st)):
            if st[j][k] != char:
                return lcp
        else:
            lcp = lcp + char
            k += 1
    return lcp
st = ['flight', 'flow', 'fly']
print(longestCommonPrefix(st))

def longestSubString(st):
    maps = {}
    max_lenght = start = 0
    for i in range(len(st)):
        if st[i] in maps:
            start = maps[st[i]] + 1
        else:
            max_lenght = max(max_lenght, i - start + 1)
        maps[st[i]] = i
    return max_lenght

st = 'abcdefaghijb'
print(longestSubString(st))


def maxSubArray(nums):
    max_total= max_sum = nums[0]
    for i in nums[1:]:
        max_total = max(i, i + max_total)
        max_sum = max(max_sum, max_total)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))


def subArraySum(nums, target):
    d = {0:1}
    count = 0
    s = 0
    for num in nums:
        s += num
        if s - target in d:
            count += d[s-target]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return count

nums = [3,4,7,2,-3,1,4,2,1]
target = 7
print(subArraySum(nums, target))

def sumTwo(ls, target):
    res = set()
    ls.sort()
    for left in range(len(ls)):
        right = len(ls) -1
        while left < right:
            if ls[left] + ls [right] == target:
                res.add((ls[left], ls[right]))
            if ls[left] + ls [right] < left:
                left +=1
            else:
                right -= 1
    return res
ls = [1,3,0,8,7,4,2,5,6]
target = 7
print(sumTwo(ls, target))

new = []
for item in list(range(2, 100)):
    for i in range(2, item):
        if item % i ==0:
            break
    else:
        new.append(item)
print(new)


def reverseNum(num):
    newNum = 0
    while num > 0:
        remain = num % 10
        newNum = newNum * 10 + remain
        num = num //10
    return newNum

print(reverseNum(12345))


st = 'Alok'
print(st[::-1])

res = ''
for i in st:
    res = i + res

print(res)



def romanInt(st):
    rDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    curr = 0
    total = 0
    for i in st:
        curr = rDict[i]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total = total + curr
        prev = curr
    return total
print(romanInt('VI'))


ls = [41,0,4,2,10,23,9,55]
fmax = ls[0]
smax = ls[0]
for i in ls[1:]:
    if fmax < i:
        smax = fmax
        fmax = i
    elif smax < i:
        smax = i
print(smax)


for i in range(5):
    for j in range(i):
        print('*', end = ' ')
    print('\t')


for i in range(6):
    for j in range(i):
        print(j , end = ' ')
    print('\n')

def subSequenceList(inpt):
    temp = [inpt[0]]
    res = []
    for i in inpt[1:]:
        if temp[-1] != i -1 :
            res.append(temp)
            temp = [i]
        else:
            temp.append(i)
    res.append(temp)   
    return res
inpt = [1,2,3,6,7,10,11,12,13,15,17,18]
output = [[1,2,3],[6,7],[10,11,12,13], [15],[17,18]]

print(subSequenceList(inpt))

def quadSum(arr, target):
    arr.sort()
    res = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            left = j + 1
            right = len(arr) -1
            while left < right :
                s = arr[i] + arr[j] + arr[left] + arr[right]
                if s == target:
                    res.append([arr[i] , arr[j], arr[left],arr[right]])
                if s < target:
                    left += 1
                else:
                    right -= 1
    return res
arr = [-1,0,-2,-1,2]
target = 0
print(quadSum(arr, target))


def threeSum(arr, target):
    res = []
    arr.sort()
    for i in range(len(arr) -2 ):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == target:
                res.append([arr[i] ,arr[left],arr[right]])
            if s < target:
                left += 1
            else:
                right -= 1
    return res


arr = [-1,0,1,-2,-4,2, -3,]
target = 0
print(threeSum(arr, target))



arr = [11, 16,12,0,2,55,23,15]
fmax = arr[0]
smax = arr[0]
tmax = arr[0]

for i in arr[1:]:
    if i > fmax:
        tmax = smax
        smax = fmax
        fmax = i
    elif i> smax:
        tmax = smax
        smax = i
    elif i > tmax:
        tmax = i
print(tmax)

def threeSumClosest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums) - 2):
        left = i+1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s- target) < abs(res - target):
                res = s
            elif s < target:
                left += 1
            else:
                right -= 1
    return res

nums= [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))

'''
import paramiko

client = paramiko.SSHClient()
client.set_missing_keyPolicy(paramiko.AutoAddPolicy())
cleint.connect(ip, username, password)

'''



'''
Pexpect is the python module to spwaning the the child the application and control then automatically. Pexpect can be use for interactive application such as ssh, ftp, password, talnet etc.
'''

ls = [3,2,5,6,10,8,0]
for i in range(len(ls)):
    for j in range(len(ls)):
        if ls[i] < ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)

substrings = []
str1 = 'alokverma'
for i in range(0,len(str1)+1) :
    for j in range(0,len(str1)+1) :
        
      
            substring = str1[i:j]
            #substring2 = str1 [j:i]
            #substring3 = str1 [i:j]
            
            if len(substring)>=1 :
                substrings.append(substring)
                #substrings.append(substring2)
            #substrings.append(substring3)
            

        
print(substrings)


