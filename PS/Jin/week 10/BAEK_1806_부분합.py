import sys

N, S = list(map(int, sys.stdin.readline().strip().split()))
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
# print(arr)

# 부분합
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
# print(arr)

# 투포인터
s, e = 0, 1
answer = 100000000
while s < N and e <= N:
    if arr[e] - arr[s] >= S:
        answer = min(answer, e-s)
        s += 1
    else:
        e += 1

# 가능한 경우가 없으면 0 출력
if answer == 100000000:
    answer = 0
print(answer)