def intersection(nums1, nums2):
    freq = {}
    result = []

    for num in nums1:
        freq[num] = 1   # mark presence

    for num in nums2:
        if num in freq:
            result.append(num)
            del freq[num]   # avoid duplicates

    return result
