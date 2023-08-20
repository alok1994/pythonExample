import re

with open('email.txt', 'r') as fr:
    fout = fr.read()
    email = re.findall(r'[\d\w\.]+\@[\d\w]+', fout)
print(email)
