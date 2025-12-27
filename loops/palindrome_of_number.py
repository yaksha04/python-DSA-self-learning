n=int(input("enter n: "))
rev=0
temp =n
while n!=0:
    digit=n%10
    rev=rev*10 + digit
    n//=10
if temp==rev:
    print("palindrome") 
else:
    print("not a palindrome")       