d = {'a': 2, 'b': 3, 'c':1}
print(d)
sorted_d = sorted(d.items(), key = lambda x : x[1])
print(sorted_d)


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

print(fact(5))
        
def argStar(arg, *args, **kwargs):
    print(arg)
    print(args)
    print(kwargs.items())

argStar('alok', 1,2,3, first='alok', second='kumar')

def balancePar(strs):
    openP = set('({[')
    matchP = set([('(', ')'), ('[',']'), ('{', '}')])
    stack = []
    for i in strs:
        if i in openP:
            stack.append(i)
        else:
            if len(stack) < 1:
                return False
            char = stack.pop()
            if (char, i) not in matchP:
                return False
    return len(stack) == 0


print(balancePar('{[]}'))



class A:
    def __init__(self, firstName):
        self.firstName = firstName

    def printFirstName(self):
        print('First Name', self.firstName)

class B(A):
    def __init__(self, middleName, firstName):
        self.middleName = middleName
        A.__init__(self, firstName)

    def printFirstMiddleName(self):
        print('first Name and middle name', self.firstName, self.middleName)

class C(B):
    def __init__(self, lastName, middleName, firstName):
        self.lastName = lastName
        B.__init__(self, middleName, firstName)

    def printFullName(self):
        print('Full Name:', self.firstName, self.middleName, self.lastName)

obj = C('Verma', 'Kumar', 'Alok')
obj.printFullName()



# Decorater is the very powerful and usefull tool in python since it allow progrommer to modify/extend the behaviour of funcation without changen in function.
def smartDivide(func):
    def inner(a,b):
        print('Going to divide {} by {}'.format(a,b))
        if b == 0:
            print("Ohh cann't divide via zero")
            return
        return func(a,b)
    return inner

@smartDivide
def divide(a,b):
    print(a/b)

divide(4,0)

def compress(strs):
    res = ''
    count = 1
    for i in range(1, len(strs)):
        if strs[i-1] == strs[i]:
            count += 1
        else:
            if count > 1:
                res = res + str(count)
            res = res + strs[i-1]
            count = 1
    if count > 1:
        res = res + str(count)
    res = res + strs[-1]
    return res

print(compress('ABBCCCDDDDEA'))


print('File __name__:', __name__)

if __name__ == '__main__':
    print('File directly executed')
else:
    print('File imported and executed')


ls = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x % 2 != 0 , ls)))

print(list(map(lambda x: x*2, ls)))

def longestPrefix(strs):
    minl = len(strs[0])
    for i in strs[1:]:
        minl = min(minl, len(i) )
    lcp = ''
    i = 0
    while i < minl:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if char != strs[j][i]:
                return lcp
        else:
            lcp = lcp + char
        i = i + 1
        

strs= ['flower', 'flow', 'flight']
print(longestPrefix(strs))

def longestSubString(st):
    d = {}
    start = 0
    maxL = 0
    for i in range(len(st)):
        if st[i] in d:
            start = d[st[i]] + 1
        else:
            maxL = max(maxL, i - start + 1)
        d[st[i]] = i
    return maxL

st = 'abcdaefg'
print(longestSubString(st))



def maxSubArray(arr):
    max_sum = max_total = arr[0]
    for i in arr[1:]:
        max_total = max(i, i + max_total)
        max_sum = max(max_sum, max_total)
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(arr))

def sumTwoNumbers(ls, target):
    ls.sort()
    res = set()
    for i in range(len(ls)):
        left = i
        right = len(ls) - 1
        while left < right:
            s = ls[left] + ls[right]
            if s == target:
                res.add((ls[left], ls[right]))
            if s < target:
                left += 1
            else:
                right -= 1
    return res

ls = [1,3,0,8,7,4,2,5,6]
target = 7
print(sumTwoNumbers(ls, target))



new = []
ls = list(range(2,100))
#print(ls)
for i in ls:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        new.append(i)
print(new)


txt = '''
555-555-5555
555 555 5555
55555555555
'''

import re
phone = re.findall(r'\d{3}[\s-]?\d{3}[\s-]?\d{4}', txt)
print(phone)


txt = '''
The first season of Indian Premiere league (IPL) was played in 2008.
The second season was played in 2009 in South Africa.
Last season was played in 2018 and won by Chennai Super kings (CSK).
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
'''

years = re.findall(r'[1-9]\d{3}', txt)
print(years)


txt = '''
file1.txt
file_one.txt
file09.txt
fil.txt
file23.txt
file.txt
'''
files = re.findall(r'file\d+\.txt',txt)
print(files)


def reverseNumber(num):
    res = 0
    while num > 0:
        rem = num % 10
        res = res*10 + rem 
        num = num // 10
    print(res)
reverseNumber(12345)



def romanInt(st):
    total = 0
    curr = 0
    prev = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in st:
        curr = rom[i]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total

print(romanInt('IV'))

ls = [1,3,2,220,39,200,202,20,203]
fmx = ls[0]
smx = ls[0]
for i in ls[1:]:
    if fmx < i:
        smx = fmx
        fmx= i
    elif smx < i and i != fmx:
        smx = i
print(smx)

def subArraySum(nums, target):
    sumDict = {0:1}
    count = 0
    s = 0
    for num in nums:
        s += num
        if s - target in sumDict:
            count += sumDict[s-target]
        if s in sumDict:
            sumDict[s] += 1
        else:
            sumDict[s] = 1
    return count

nums = [3,4,7,2,-3,1,4,2,1]
target = 7
print(subArraySum(nums, target))

def subSequenceArray(inpt):
    curr = [inpt[0]]
    res = []
    for i in inpt[1:]:
        if i - 1 != curr[-1]:
            res.append(curr)
            curr = [i]
        else:
            curr.append(i)
    res.append(curr)
    print(res)

inpt = [1,2,3,6,7,10,11,12,13,15,17,18]
subSequenceArray(inpt)
output = [[1,2,3],[6,7],[10,11,12,13], [15],[17,18]]

def sumOfQuad(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    res.add((nums[i] , nums[j] , nums[left] , nums[right]))
                    left += 1
                    right -= 1
                if s < target:
                    left += 1
                else:
                    right -= 1
    return res

nums=[-1,0,-2,-1,2]
target = 0
print(sumOfQuad(nums, target))

def threeSumClosest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            sumhere = nums[i] + nums[left] + nums[right]
            if abs(sumhere - target) < abs(res - target):
                res = sumhere
            if sumhere < target:
                left += 1
            else:
                right -=1
    return res

nums= [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))
def order(num):
    n = 0
    while num !=0:
        n += 1
        num = num // 10
    return n

def armstrong(num):
    ords = order(num)
    temp = num
    s = 0
    while num != 0:
        remain = num % 10
        s += remain ** ords
        num = num // 10

    print(s)
    
armstrong(1634)

import json

with open('text.json', 'r') as fr:
    data = json.loads(fr.read())
    for i in data["emp_details"]:
        print(i)


ls1 = [10,9,3,1,4,6,12,0]
new = []
while ls1:
    minimum = ls1[0]
    for i in ls1:
        if i < minimum:
            minimum = i
    new.append(minimum)
    ls1.remove(minimum)
print(new)


l = [64,12,19,121,129,50,64,90,13,17,23] 
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j],l[i]
print(l)


nums = list(range(1,10))
for i in nums:
    if i % 2 ==0 and i % 3 ==0:
        print('A,B')
    elif i %2 ==0:
        print('A')
    elif i % 3 == 0:
        print('B')
    else:
        print(i)

ls = [1,23,4,5,6,7,9,10]
obj = iter(ls)
print(next(obj))
print(next(obj))


from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name,birthyear):
        return cls(name, date.today().year - birthyear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age) )


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John', 1983)
person1.display()


class Student:

    @staticmethod
    def is_fullname(name):
        names = name.split(' ')
        return len(names) > 1

print(Student.is_fullname('Alok Kumar'))
