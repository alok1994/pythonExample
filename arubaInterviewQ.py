import re
str1 = '''Name    Age    Log
----------------------------
Alok    16    My Name is alok'''
splitList = str1.split('----------------------------')
splitL1 = re.sub(r'\n', '',splitList[0]).split('    ')
splitL2 = re.sub(r'\n', '',splitList[1]).split('    ')
d = dict(zip(splitL1, splitL2))
print(d)
