arr = [11, 16,12,0,2,55,23,15]
first = arr[0]
second = arr[0]
third = arr[0]
for i in range(1, len(arr)):
    if arr[i] > first:
        third = second
        second = first
        first = arr[i]
    elif arr[i] > second:
        third = second
        second = arr[i]
    elif arr[i] > third:
        third = arr[i]
print(third)
