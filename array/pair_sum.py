def pair_sum(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return True
        elif s < target:
            i += 1
        else:
            j -= 1
    return False
