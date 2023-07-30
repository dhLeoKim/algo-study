from sys import stdin
from collections import deque

stdin = open("input/BAEK_7562_나이트의_이동.txt")

T = int(stdin.readline().rstrip())
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def BFS(a, b, c, d):
    q = deque()
    q.append((a, b))
    visited[a][b] = 0

    while q:
        (u, v) = q.popleft()
        if u == c and v == d:
            print(visited[u][v])
            return
        
        for i in range(8):
            if 0 <= u+dx[i] < I and 0 <= v+dy[i] < I and visited[u+dx[i]][v+dy[i]] == -1:
                q.append((u+dx[i],v+dy[i]))
                visited[u+dx[i]][v+dy[i]] = visited[u][v] + 1

for _ in range(T):
    I = int(stdin.readline().rstrip())
    a, b = tuple(map(int, stdin.readline().rstrip().split()))
    c, d = tuple(map(int, stdin.readline().rstrip().split()))
    visited = [[-1]*I for _ in range(I)]  # 이동할 때마다 +1
    BFS(a, b, c, d)