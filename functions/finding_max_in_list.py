def max(l1):
    max=l1[0]
    for num in l1:
        if num>max:
            max=num
    return max
print(max([2,3,4,5,6,7,0]))        