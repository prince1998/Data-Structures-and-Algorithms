# Avg of contiguous subarrays - Sliding Window Pattern
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5
average = []
window_end = 0
window_start = 0 
window_sum = 0

for window_end in range(0,len(arr)): 
    window_sum += arr[window_end]
    if window_end >= K-1:
        average.append(window_sum/K)
        window_sum -= arr[window_start]
        window_start += 1
    
print(average)