import sys
import itertools
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().strip().split())

visited = [[0] * N for _ in range(N)]
lab = []
virus = []
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 999999999
for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if temp[j] == 1:
            visited[i][j] = -1
        if temp[j] == 2:
            virus.append([i, j])
    lab.append(temp)
# print(lab)


# bfs
def bfs(d):
    global cnt
    while d:
        a, b = d.popleft()
        for di, dj in dd:
            if 0 <= a+di < N and 0 <= b+dj < N and d_visited[a+di][b+dj] == 0:
                d_visited[a+di][b+dj] = d_visited[a][b] + 1
                d.append([a+di, b+dj])
    else:
        t = 0
        for i in range(N):
            for j in range(N):
                t = max(t, d_visited[i][j] - 1)
                if d_visited[i][j] == 0:
                    return
        else:
            cnt = min(cnt, t)

# 바이러스 M개
v = list(itertools.combinations(virus, M))

for vv in v:
    d = deque()
    d.extend(list(vv))
    d_visited = copy.deepcopy(visited)
    for vvv in list(vv):
        d_visited[vvv[0]][vvv[1]] = 1
    bfs(d)

if cnt == 999999999:
    print(-1)
else:
    print(cnt)