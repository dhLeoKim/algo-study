import sys
sys.stdin = open('input_1149.txt')
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

# 초기값 dp[0][j]는 주어진 값 그대로

for i in range(1, N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2]) # i번째를 빨강으로 할 때, 현재까지의 비용 최솟값
    dp[i][1] += min(dp[i-1][2], dp[i-1][0]) # i번째를 초록으로 할 때, 현재까지의 비용 최솟값
    dp[i][2] += min(dp[i-1][0], dp[i-1][1]) # i번째를 파랑으로 할 때, 현재까지의 비용 최솟값

print(min(dp[N-1]))