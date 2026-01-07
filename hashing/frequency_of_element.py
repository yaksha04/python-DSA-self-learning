def frequency(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq

print(frequency([1,2,2,3,1,1]))
