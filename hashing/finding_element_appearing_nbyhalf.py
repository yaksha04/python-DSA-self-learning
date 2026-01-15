def majority_element(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
        if freq[n] > len(nums)//2:
            return n

print(majority_element([2,2,1,2,3,2,2]))
print(majority_element([3,3,4,2,4,4,2,4,4]))  # Example usage