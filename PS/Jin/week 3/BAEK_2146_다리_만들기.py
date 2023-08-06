# pypy3으로 제출

from collections import deque

N = int(input())
islands = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# print(islands)
# print(visited)

# bfs 2번 사용

# 1. 섬 구분
def bfs1(a, b):
    global num
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    while q:
        i, j = q.popleft()
        islands[i][j] = num
        for di, dj in d:
            if 0 <= i + di < N and 0 <= j + dj < N and islands[i+di][j+dj] and visited[i+di][j+dj] == 0:
                visited[i+di][j+dj] = 1
                q.append([i+di, j+dj])

# 2. 다리 연결
def bfs2(b):
    global minV
    q = deque()
    for i in range(N):
        for j in range(N):
            if islands[i][j] == b:
                visited2[i][j] = 1
                q.append([i, j])
    while q:
        i, j = q.popleft()
        if islands[i][j] != 0 and visited2[i][j] != 1:
            minV = min(minV, visited2[i][j] - 2)
        else:
            for di, dj in d:
                if 0 <= i+di < N and 0 <= j+dj < N and visited2[i+di][j+dj] == 0:
                    visited2[i+di][j+dj] = visited2[i][j] + 1
                    q.append([i+di, j+dj])

# 1. 섬 구분
num = 1
for i in range(N):
    for j in range(N):
        if islands[i][j] == 1 and visited[i][j] == 0:
            bfs1(i, j)
            num += 1

# 2. 다리 연결
minV = N * N
for b in range(1, num):
    visited2 = [[0] * N for _ in range(N)]
    bfs2(b)

# print(islands)
print(minV)