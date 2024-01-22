import sys
sys.stdin = open('input_17141.txt')
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

def dfs(idx):
    global ret

    if len(virus) == M:
        t = bfs(virus)
        ret = min(t, ret)
        return
    
    for num in range(idx, L):
        if num not in virus:
            virus.append(num)
            dfs(num+1)
            virus.pop()


def bfs(virus):
    visited = []
    for i in range(N):
        visited.append(visited_lst[i][:])
    
    queue = deque()
    for idx in virus:
        i, j = virus_lst[idx]
        visited[i][j] = 0
        queue.append((i, j, 0))

    while queue:
        i, j, t = queue.popleft()
        di, dj = [0, -1, 0, 1], [1, 0, -1, 0]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
                queue.append((ni, nj, t+1))
                visited[ni][nj] = t+1
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                return 1e9

    return t


visited_lst = [[-1]*N for _ in range(N)]
virus_lst = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            virus_lst.append((i, j))
        elif lst[i][j] == 1:
            visited_lst[i][j] = '-'

L = len(virus_lst)
virus = []
ret = 1e9
dfs(0)

print(-1 if ret == 1e9 else ret)