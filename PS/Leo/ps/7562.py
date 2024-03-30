import sys
sys.stdin = open('input_7562.txt')
input = sys.stdin.readline

from collections import deque

def bfs(si, sj):
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append((si, sj, 0))
    visited[si][sj] = True

    di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        i, j, cnt = queue.popleft()
        if i == ei and j == ej:
            return cnt

        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj, cnt+1))


tc = int(input())
for _ in range(tc):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    board = [[0]*N for _ in range(N)]

    ret = bfs(si, sj)
    print(ret)