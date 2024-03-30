import sys
sys.stdin = open('input_16234.txt')
input = sys.stdin.readline

from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    temp = [(i, j)]
    temp_sum = lst[i][j]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(lst[i][j]-lst[ni][nj]) <= R:
                queue.append((ni, nj))
                visited[ni][nj] = True
                temp.append((ni, nj))
                temp_sum += lst[ni][nj]

    temp_ret = temp_sum // len(temp)
    for i, j in temp:
        lst[i][j] = temp_ret


N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
ret = 0
flag = True
while flag:
    flag = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and not visited[i][j] and L <= abs(lst[i][j]-lst[ni][nj]) <= R:
                    bfs(i, j)
                    flag = True

    if flag:
        ret += 1

print(ret)