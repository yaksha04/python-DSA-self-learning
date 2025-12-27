n=int(input("num: "))
temp=n
sum=0
digits=len(str(n))
while n!=0:
    digit=n%10
    sum=sum+digit**digits
    n//=10
if sum==temp:
    print("armstrong number")
else:
    print("not an armstrong number")        