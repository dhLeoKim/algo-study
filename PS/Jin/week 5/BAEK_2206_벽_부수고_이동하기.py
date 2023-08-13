from collections import deque

N, M = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# breaking_cnt = 0
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# q = deque()
# q.append([0, 0, 0])
# visited[0][0][0] = 1
# while q:
#     x, y, z = q.popleft()
#     if x == N-1 and y == M-1:
#         print(visited[x][y][z])
#         break
#     for di, dj in d:
#         if 0 <= x+di < N and 0 <= y+dj < M:
#             if arr[x+di][y+dj] == 0 and visited[x+di][y+dj][z] == 0:
#                 visited[x+di][y+dj][z] = visited[x][y][z] + 1
#                 q.append([x+di, y+dj, z])
#             elif arr[x+di][y+dj] == 1 and z == 0:
#                 visited[x+di][y+dj][1] = visited[x][y][z] + 1
#                 q.append([x+di, y+dj, 1])
# else:
#     print(-1)

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for di, dj in d:
            if 0 <= x+di < N and 0 <= y+dj < M:
                if arr[x+di][y+dj] == 0 and visited[x+di][y+dj][z] == 0:
                    visited[x+di][y+dj][z] = visited[x][y][z] + 1
                    q.append([x+di, y+dj, z])
                elif arr[x+di][y+dj] == 1 and z == 0:
                    visited[x+di][y+dj][1] = visited[x][y][z] + 1
                    q.append([x+di, y+dj, 1])
    else:
        return -1

print(bfs())