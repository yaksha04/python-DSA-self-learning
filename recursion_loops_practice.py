def print_numbers(n):
    if n == 0:        # base case
        return
    print_numbers(n-1)
    print(n)

print_numbers(5)
print("============================")
def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n-1)

print_reverse(5)
print("============================")

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))
print("============================")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print("============================")
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n//10)

print(count_digits(12345))
print("============================")

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)

print(sum_digits(123))
print("============================")
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))

print("============================")
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))

print("============================")
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))

print("============================")
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

print(power(2, 4))

print("============================")
numbers = [1,2,3,4,5,6]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)

print("============================")
n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("============================")
numbers = [4, 9, 2, 7, 1]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
print("============================")

year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
