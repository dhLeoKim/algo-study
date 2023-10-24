from sys import stdin, setrecursionlimit
setrecursionlimit(250000)

stdin = open("input/BOJ_1520_내리막_길.txt")

M, N = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(M)]
memo = [[-1]*N for _ in range(M)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dfs(x, y):
    if (x, y) == (M-1, N-1):
        return 1
    
    if memo[x][y] != -1:
        return memo[x][y]
    
    memo[x][y] = 0

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[x][y] > graph[nx][ny]:
            memo[x][y] += dfs(nx, ny)
    
    return memo[x][y]

print(dfs(0, 0))
