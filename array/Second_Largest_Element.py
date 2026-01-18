largest = second = -1
arr=[1,234,3,2,4,5,3,5]
for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x != largest and x > second:
        second = x
