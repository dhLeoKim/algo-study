import sys
from heapq import heappush, heappop

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d_bus, a_bus, c = map(int, sys.stdin.readline().strip().split())
    graph[d_bus].append([a_bus, c])

def dijkstra(k):
    h = []
    d[k] = 0
    heappush(h, (0, k))
    while h:
        dist_u, u = heappop(h)
        if dist_u > d[u]:
            continue
        for v, w in graph[u]:
            dist_v = dist_u + w
            if dist_v < d[v]:
                d[v] = dist_v
                nearest[v] = u
                heappush(h, (dist_v, v))

d_bus, a_bus = map(int, input().split())
INF = 1e9
nearest = [0] * (n+1)
d = [INF] * (n+1)

dijkstra(d_bus)
answer = [a_bus]
now = a_bus
while now != d_bus:
    now = nearest[now]
    answer.append(now)

print(d[a_bus])
print(len(answer))
print(*list(reversed(answer)))