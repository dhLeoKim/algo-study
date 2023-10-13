import sys
from collections import deque

N, L, R = map(int, input().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(i, j, temp):
    q = deque()
    q.append([i, j])
    cntry = 1
    total = arr[i][j]
    while q:
        x, y = q.popleft()
        for di, dj in dd:
            if 0 <= x + di < N and 0 <= y + dj < N and visited[x+di][y+dj] == 0 and L <= abs(arr[x][y] - arr[x+di][y+dj]) <= R:
                visited[x+di][y+dj] = temp
                cntry += 1
                total += arr[x+di][y+dj]
                q.append([x+di, y+dj])
    else:
        if cntry != 1:
            for i in range(N):
                for j in range(N):
                    if visited[i][j] == temp:
                        arr[i][j] = int(total/cntry)

cnt = 0
while True:
    temp = 1
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = temp
                bfs(i, j, temp)
                temp += 1
    else:
        if temp == N*N + 1:
            break
        else:
            cnt += 1
print(cnt)