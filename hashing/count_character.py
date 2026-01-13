def char_count(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_count("devoops"))
print(char_count("hello world"))  # Example usage