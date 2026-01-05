arr=[1,2,3,2,1,2,3,2,1,3,4,5,6,7,8,6,5]
frequency={}
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
max_frequency=0
for j in frequency:
    if frequency[j]>max_frequency:
        max_frequency=frequency[j]
    
print(max_frequency)

total=0
for k in frequency:
    if frequency[k]==max_frequency:
        total=total+1

print(total)        
