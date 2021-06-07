# Maximum sum subarray of size K - Brute Force

arr = [2, 1, 5, 1, 3, 2]
K = 3
max_sum = 0

for i in range(0,len(arr)-(K)+1):
    sum = 0
    for j in range(i,i+K):
        sum += arr[j]
    if max_sum < sum:
        max_sum = sum

print(max_sum)

