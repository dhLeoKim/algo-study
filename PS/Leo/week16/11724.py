import sys
sys.stdin = open('input_11724.txt')
input = sys.stdin.readline

from collections import deque

def bfs(now):
    queue = deque()
    queue.append(now)
    visited[now] = True

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ret = 0
visited = [False]*(N+1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ret += 1

print(ret)