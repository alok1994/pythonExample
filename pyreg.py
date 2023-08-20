import re


# Example 1: Find all the matched for dog and dogs in the given text

txt = 'I have 2 dogs. One dog is 1 year old and other one is 2 years old. Both dogs are very cute'

pattern = re.compile('dogs?')

print(pattern.findall(txt))


# Example 2 : Find all filenames starting with file and ending with .txt in given text

txt = '''
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
'''

pattern = re.compile('file\w*\.txt')

print(pattern.findall(txt))

# Example 3: Find all filenames starting with file followed by 1 or more digits and
# ending with .txt in given txt

txt = '''
file1.txt
file_one.txt
file09.txt
fil.txt
file23.txt
file.txt
'''

pattern = re.compile('file\d+\.txt')
print(pattern.findall(txt))



# Example 4: Find the years in the given txt

txt = '''
The first season of Indian Premiere league (IPL) was played in 2008.
The second season was played in 2009 in South Africa.
Last season was played in 2018 and won by Chennai Super kings (CSK).
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
'''

pattern = re.compile('[1-9]\d{3}')
print(pattern.findall(txt))


# Example: Write a pattern to validat telephone numbers.
txt = '''
555-555-5555
555 555 5555
55555555555
'''

pattern = re.compile('\d{3}[\s-]?\d{3}[\s-]?\d{4}')
print(pattern.findall(txt))


txt = '''
10.20.10.2
0.0.0.0
192.168.10.3
'''

pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
print(pattern.findall(txt))
