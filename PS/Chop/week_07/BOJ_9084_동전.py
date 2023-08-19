from sys import stdin

stdin = open("input/BOJ_9084_동전.txt")

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    coins.insert(0, 0)
    M = int(stdin.readline())

    dp = [[0] * (M+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j]
            if j-coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    print(dp[N][M])