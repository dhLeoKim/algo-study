import sys

N = int(sys.stdin.readline().strip())
arr = list(list(map(int, sys.stdin.readline().strip().split())))

total_arr = [0] * len(arr)
total_arr[0] = arr[0]

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            total_arr[i] = max(total_arr[j] + arr[i], total_arr[i])
        else:
            total_arr[i] = max(total_arr[i], arr[i])

# print(total_arr)
print(max(total_arr))