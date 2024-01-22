import sys

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
maxV = 0

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def dfs(i, j, total, dep):
    global maxV
    if dep == 4:
        maxV = max(maxV, total)
        return
    for di, dj in d:
        if 0 <= i + di < N and 0 <= j + dj < M and visited[i+di][j+dj] == 0:
            visited[i+di][j+dj] = 1
            dfs(i+di, j+dj, total+arr[i+di][j+dj], dep+1)
            visited[i+di][j+dj] = 0


def tet(i, j):
    global maxV
    for k in range(4):
        total = arr[i][j]
        for dd in range(3):
            ddd = (k+dd) % 4
            if 0 <= i+d[ddd][0] < N and 0 <= j+d[ddd][1] < M:
                total += arr[i+d[ddd][0]][j+d[ddd][1]]
            else:
                total = arr[i][j]
                break
        maxV = max(maxV, total)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0
        # 테트리스 모양 (분홍색)
        tet(i, j)
print(maxV)