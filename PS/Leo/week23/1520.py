import sys
sys.stdin = open('input_1520.txt')
input = sys.stdin.readline

sys.setrecursionlimit(10**9)
from collections import deque

def dfs(i, j):
    global ret

    if i == M-1 and j == N-1:   # 도착지에 도달
        return 1

    if dp[i][j] == -1:          # -1로 방문여부 확인
        dp[i][j] = 0

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < M and 0 <= nj < N and lst[i][j] > lst[ni][nj]:
                dp[i][j] += dfs(ni, nj)

    # -1이 아니라면 이미 방문한 적이 존재
    # 더 진행할 필요 없이 현재까지의 dp값을 반환하여 
    # 도착지까지의 경우의 수를 업데이트
    return dp[i][j]


M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

# dp : 도착지까지 가는 경우의 수는 
# 도착지까지 갈 수 있는 임의의 점들에서 
# 도착지점까지 가는 경우의 수를 합한 것과 같다.
dp = [[-1]*N for _ in range(M)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

print(dfs(0, 0))