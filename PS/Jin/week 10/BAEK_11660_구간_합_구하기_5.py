import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
arr = [[0] * (N+1)]
for _ in range(N):
    arr.append([0] + list(map(int, sys.stdin.readline().strip().split())))
# print(arr)

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        # arr[0][0]에서 arr[i][j]의 직사각형에 해당하는 총합 계산
        arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
# print(arr)

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().strip().split()))
    total = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(total)
