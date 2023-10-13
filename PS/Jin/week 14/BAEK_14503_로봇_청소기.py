import sys
from collections import deque

dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
q = deque()
q.append([r, c])
visited[r][c] = 1
while q:
    i, j = q.popleft()
    if visited[i][j] == 1:
        cnt += 1
    # print(i, j)
    # 회전
    for _ in range(4):
        d = (d + 3) % 4
        di, dj = dd[d]
        if 0 <= i + di < N and 0 <= j + dj < M:
            if arr[i+di][j+dj] == 0 and visited[i+di][j+dj] == 0:
                visited[i+di][j+dj] = 1
                q.append([i+di, j+dj])
                break
    # 빈 칸이 없는 경우
    else:
        di, dj = dd[(d + 2) % 4]
        if 0 <= i + di < N and 0 <= j + dj < M and arr[i+di][j+dj] == 0:
            visited[i+di][j+dj] += 1
            q.append([i+di, j+dj])
        else:
            break
print(cnt)