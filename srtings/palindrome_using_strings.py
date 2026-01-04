text='yaksha'
reverse=""
for word in text:
    reverse=word+reverse
if reverse==text:
    print(" the word is palindrome")
else:
    print("the word is not palindrome")    