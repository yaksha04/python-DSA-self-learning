def longest_word(words):
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest    
print(longest_word(["hello", "world", "python","ai","cow","apple"]))    