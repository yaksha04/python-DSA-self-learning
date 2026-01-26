arr=[1,2,3]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        print(arr[i:j+1])


arr=[-1,-3,4,3,4,-6,4,7,-2,7]
def kadanes_algorithm(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(num[i],current_sum+num[i])
        max_sum=max(current_sum,max_sum)
    return max_sum    
print(kadanes_algorithm(arr))
