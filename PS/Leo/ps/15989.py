import sys
sys.stdin = open('input_15989.txt')
input = sys.stdin.readline

dp = [[0]*10001 for _ in range(4)]
dp[1][1] = 1
dp[2][2] = 1
dp[1][2] = 1
dp[3][3] = 1
dp[1][3] = 2

for i in range(4, 10001):
    dp[3][i] = dp[3][i-3]
    dp[2][i] = dp[2][i-2] + dp[3][i-2]
    dp[1][i] = dp[1][i-1] + dp[2][i-1] + dp[3][i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[1][N] + dp[2][N] + dp[3][N])