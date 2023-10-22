import sys
from collections import deque
N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    adjList[u].append(v)
    adjList[v].append(u)

def bfs(i):
    q = deque([i])
    while q:
        x = q.popleft()
        for nxt in adjList[x]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        visited[i] = 1
        bfs(i)
print(cnt)