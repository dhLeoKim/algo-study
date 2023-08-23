import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())

dp = [[0] * N for _ in range(N)]

# 한 자리인 경우
for i in range(N):
    dp[i][i] = 1
# 두 자리인 경우
for i in range(N-1):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1
# 그 외의 경우
# 대각선 순서로 채우기
for cnt in range(N-2):
    for i in range(N-2-cnt):
        j = i+2+cnt
        # print(i, j)
        if num[i] == num[j]:
            dp[i][j] = dp[i+1][j-1]
# print(dp)

for _ in range(M):
    S, E = list(map(int, sys.stdin.readline().strip().split()))
    print(dp[S-1][E-1])