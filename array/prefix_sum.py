def subarray_sum_k(arr, k):
    prefix_sum = 0
    seen = {0: 1}

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in seen:
            return True
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return False
