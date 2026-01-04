def reverse(text):
    rev=""
    for ch in text:
        rev=ch+rev
    return rev
print(reverse("devops"))    