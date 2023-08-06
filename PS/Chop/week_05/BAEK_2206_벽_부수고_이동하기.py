from sys import stdin
from collections import deque

stdin = open("input/BAEK_2206_벽_부수고_이동하기.txt")

N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    q = deque([(0, 0, False)])
    visited[0][0][0] = 1

    while q:
        x, y, isBroken = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][0] if not isBroken else visited[x][y][1]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not graph[nx][ny]:
                    if isBroken and not visited[nx][ny][1]:
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        q.append((nx, ny, isBroken))
                    elif not isBroken and not visited[nx][ny][0]:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        q.append((nx, ny, isBroken))
                elif graph[nx][ny] and not isBroken and not visited[nx][ny][0]:
                    q.append((nx, ny, True))
                    visited[nx][ny][1] = visited[x][y][0] + 1
    return -1

print(bfs())