import sys
sys.stdin = open('input_9095.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())

    dp = [[0, 0, 0] for _ in range(N+5)]

    dp[1] = [1, 0, 0]
    dp[2] = [1, 1, 0]
    dp[3] = [2, 1, 1]
    
    if N >= 4:
        for i in range(4, N+1):
            dp[i][0] = sum(dp[i-1])
            dp[i][1] = sum(dp[i-2])
            dp[i][2] = sum(dp[i-3])

    print(sum(dp[N]))