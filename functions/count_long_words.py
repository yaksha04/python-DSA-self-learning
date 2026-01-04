def count_long_words(words):
    count=0
    for word in words:
        if len(word)>3:
            count=count+1
    return count
print(count_long_words(["hello", "world", "python","ai","cow","apple"]))