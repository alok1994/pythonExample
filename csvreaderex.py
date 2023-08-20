import csv

with open('detail.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    d = {}
    for item in csv_reader:
        #print (item)
        d[item[0]] = item[2]
    sort_by_value = sorted(d.items(), key =lambda x : x[1])

print(d)
print(sort_by_value)
