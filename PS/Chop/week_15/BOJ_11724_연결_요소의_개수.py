from sys import stdin
from collections import deque

stdin = open("input/BOJ_11724_연결_요소의_개수.txt")

N, M = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [True] + [False for _ in range(N)]
cnt = 0

for node in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    global cnt
    q = deque([node])

    while q:
        now = q.popleft()
        visited[now] = True
        if graph[now]:
            for next in graph[now]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
    cnt += 1

for node in range(1, N+1):
    if not visited[node]:
        bfs(node)

print(cnt)