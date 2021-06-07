# Maximum sum subarray of size K - Sliding Window

arr = [2, 1, 5, 1, 3, 2]
K = 3
max_sum = 0
window_sum = 0
window_start = 0

for window_end in range(0,len(arr)):
    window_sum += arr[window_end]
    if window_end >= K-1:
        if max_sum < window_sum:
            max_sum = window_sum
        window_sum -= arr[window_start]
        window_start += 1

print(max_sum)

