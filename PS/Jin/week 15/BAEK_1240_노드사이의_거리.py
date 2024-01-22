import sys
from collections import deque

N, M = map(int, input().split())
con = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, l = map(int, sys.stdin.readline().strip().split())
    con[n1].append([n2, l])
    con[n2].append([n1, l])


def bfs(a, b):
    visited[a] = 1
    q = deque()
    q.append([a, 0])
    while q:
        cur, d = q.popleft()
        if cur == b:
            return d
        for i, l in con[cur]:
            if visited[i] == 0:
                visited[i] = 1
                q.append([i, d+l])


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    visited = [0] * (N+1)
    length = bfs(a, b)
    print(length)