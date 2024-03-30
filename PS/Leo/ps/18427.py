import sys
sys.stdin = open('input_18427.txt')
input = sys.stdin.readline

N, M, H = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i] = dp[i-1][:]
    for k in lst[i-1]:
        for j in range(k, H+1):
            dp[i][j] += dp[i-1][j-k]

print(dp[N][H]%10007)