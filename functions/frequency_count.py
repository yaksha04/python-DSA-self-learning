arr = [1, 2, 2, 3, 1, 1, 4]

freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)