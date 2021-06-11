# Maximum sum subarray of size K - Sliding Window
import math
arr = [3, 4, 1, 1, 6]
sum_required = 8
min_len = math.inf
window_sum = 0
window_start = 0

for window_end in range(0,len(arr)):
    window_sum += arr[window_end]
    while window_sum >= sum_required:
        min_len = min(min_len,(window_end-window_start)+1)
        window_sum -= arr[window_start]
        window_start += 1
    
    if min_len == math.inf:
        print("0")

print(min_len)