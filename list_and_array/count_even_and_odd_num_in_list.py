nums=[2,4,1,56,4,2,3,33,66,75]
even=0
odd=0
for num in nums:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print("even: ",even)
print("odd: ",odd)            