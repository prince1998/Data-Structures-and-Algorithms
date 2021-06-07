# Avg of contiguous subarrays - Sliding Window Pattern
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5
average = [] 

for i in range(0,len(arr)-(K)+1): 
    sum = 0

    for j in range(i,i+K):
        sum = sum + arr[j]
    average.append(sum/K)
    
print(average)