import sys
sys.stdin = open('input_2206.txt')
input = sys.stdin.readline

from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0))
    visited[i][j][0] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        i, j, flag = queue.popleft()

        if i == N-1 and j == M-1:
            return visited[i][j][flag]
        
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if lst[ni][nj] == 1 and flag == 0:                      # 벽, 파괴 가능한 경우
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    queue.append((ni, nj, 1))
                elif lst[ni][nj] == 0 and visited[ni][nj][flag] == 0:   # 진행가능한 곳
                    visited[ni][nj][flag] = visited[i][j][flag] + 1
                    queue.append((ni, nj, flag))

    return -1


N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]    # [벽을 부수지 않은 경로, 벽을 부순 경로] 형태로 방문 표기

print(bfs(0, 0))