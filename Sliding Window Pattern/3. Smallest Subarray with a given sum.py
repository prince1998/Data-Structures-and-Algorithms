# Maximum sum subarray of size K - Sliding Window

arr = [2, 1, 5, 2, 3, 2]
sum_required = 7
window_sum = 0
window_start = 0
min_len = 200000

for window_end in range(0,len(arr)):
    window_sum += arr[window_end]
    while  window_sum>=sum_required:
        if min_len > ((window_end - window_start) + 1):
            min_len = (window_end - window_start) + 1
        window_sum -= arr[window_start]
        window_start += 1

print(min_len)

