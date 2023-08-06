from sys import stdin
from collections import deque

stdin = open("input/BAEK_2573_빙산.txt")
N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(sx, sy):
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 주변이 바다면 빙산을 녹임
                if (graph[nx][ny] == 0) and (graph[x][y] > 0):
                    graph[x][y] -= 1

                # 주변이 빙산이면 q에 append
                elif graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    # 연결된 모든 빙산을 탐색 한 경우 개수 1 return
    return 1   

year, ice_count = 0, 0
while True:
    flag = True
    ice_count = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] !=0 and visited[i][j] == 0:
                visited[i][j] = 1
                ice_count += BFS(i, j)

    # 2개 이상으로 분리 된 경우
    if ice_count > 1:
        break

    # 만일 빙산이 다 녹을 때까지 분리되지 않으면 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                flag = False
    
    if flag:
        year = 0
        break

    year += 1

print(year)