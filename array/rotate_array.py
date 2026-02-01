def rotate(nums, k):
    n = len(nums)
    k = k % n          # important
    return nums[-k:] + nums[:-k]

nums = [1,2,3,4,5]
k = 2
print(rotate(nums, k))
