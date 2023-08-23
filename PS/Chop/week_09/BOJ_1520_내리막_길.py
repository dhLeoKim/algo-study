from sys import stdin, setrecursionlimit
setrecursionlimit(250000)

stdin = open("input/BOJ_1520_내리막_길.txt")

M, N = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0


def dfs(x, y, visited):
    global ans

    if (x, y) == (M-1, N-1):
        ans += 1
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[x][y] > graph[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, visited)
            visited[nx][ny] = False


visited[0][0] = True
dfs(0, 0, visited)
print(ans)
