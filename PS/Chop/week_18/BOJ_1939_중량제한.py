from sys import stdin
from collections import deque

stdin = open("input/BOJ_1939_중량제한.txt")

N, M = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, stdin.readline().rstrip().split())
l, r = 0, int(1e9)

def bfs(mid):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        now = q.popleft()
        if now == e:
            return True

        for node, cost in graph[now]:
            if not visited[node] and mid <= cost:
                q.append(node)
                visited[node] = True

    return False

ans = 0

while l <= r:
    mid = (l + r) // 2
    visited = [False for _ in range(N+1)]

    if bfs(mid):
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid - 1

print(ans)