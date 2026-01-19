arr = [0,1,0,3,12]
res = []
zeros = 0

for x in arr:
    if x != 0:
        res.append(x)
    else:
        zeros += 1

res.extend([0]*zeros)
