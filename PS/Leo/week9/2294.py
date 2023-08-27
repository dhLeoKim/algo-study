import sys
sys.stdin = open('input_2294.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

# dp[i] = 동전의 합을 i원으로 만드는 동전 개수의 최소값
# dp[i] = min(dp[i], dp[i-A]+1)
# min{현재까지의 최소개수, 이전까지의 최소 개수 + 1(A가치 동전 하나)}
dp = [10005]*(K+1)
dp[0] = 0

for coin in lst:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(-1) if dp[K] == 10005 else print(dp[K])