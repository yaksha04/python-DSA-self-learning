# hashmap_basics.py

# ==============================
# HASHMAP BASICS IN PYTHON
# ==============================

def basic_operations():
    print("=== Basic Operations ===")

    mp = {}

    # Insert
    mp["apple"] = 2
    mp["banana"] = 5

    # Access
    print("Apple:", mp["apple"])

    # Update
    mp["apple"] = 10
    print("Updated Apple:", mp["apple"])

    # Delete
    del mp["banana"]
    print("After deletion:", mp)

    # Check key exists
    if "apple" in mp:
        print("Apple exists")


# ==============================
# FREQUENCY COUNT
# ==============================

def frequency_count(arr):
    print("\n=== Frequency Count ===")

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    print("Frequency:", freq)
    return freq


# ==============================
# FIND DUPLICATES
# ==============================

def find_duplicates(arr):
    print("\n=== Find Duplicates ===")

    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    print("Duplicates:", list(duplicates))
    return list(duplicates)


# ==============================
# TWO SUM PROBLEM
# ==============================

def two_sum(nums, target):
    print("\n=== Two Sum ===")

    mp = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in mp:
            print("Indices:", mp[diff], i)
            return [mp[diff], i]

        mp[num] = i

    print("No solution found")
    return []


# ==============================
# MAIN FUNCTION (TESTING)
# ==============================

if __name__ == "__main__":
    basic_operations()

    arr = [1, 2, 2, 3, 1, 4]
    frequency_count(arr)

    arr2 = [1, 2, 3, 1, 2]
    find_duplicates(arr2)

    nums = [2, 7, 11, 15]
    target = 9
    two_sum(nums, target)
