import sys
sys.stdin = open('input_1915.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().strip())) for _ in range(n)]

ret = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and dp[i][j] == 1:
            dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        ret = max(dp[i][j], ret)

print(ret**2)