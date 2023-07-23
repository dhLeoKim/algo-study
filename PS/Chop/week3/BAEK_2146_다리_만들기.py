from sys import stdin
from collections import deque
from pprint import pprint

stdin = open("input/BAEK_2146_다리_만들기.txt")
N = int(stdin.readline().rstrip())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
bridge = N * N

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs_land(i, j):
    visited[i][j] = 1
    graph[i][j] = num
    q = deque([(i, j)])

    while q:
        (x, y) = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 1:
                    graph[nx][ny] = num
                    q.append((nx, ny))

def bfs_sea(i, j):
    visited = [[0]*N for _ in range(N)]
    num = graph[i][j]
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        (x, y) = q.popleft()
        if visited[x][y] - 1 == bridge:
            return bridge
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] != 0 and graph[nx][ny] != num:
                    return visited[x][y] - 1
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return bridge

visited = [[0]*N for _ in range(N)]
num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and visited[i][j] == 0:
            bfs_land(i, j)
            num += 1 

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            bridge = bfs_sea(i, j)

print(bridge)