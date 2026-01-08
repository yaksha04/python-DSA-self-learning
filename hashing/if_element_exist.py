def exists(nums, target):
    seen = {}
    for n in nums:
        seen[n] = True
    return target in seen

print(exists([1,3,5,7], 5))
