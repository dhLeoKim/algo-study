import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append([v, w])

def dijkstra(k):
    h = []
    d[k] = 0
    heappush(h, (0, k))
    while h:
        dist_u, u = heappop(h)
        if dist_u > d[u]:
            continue
        for v, w in graph[u]:
            dist_v = d[u] + w
            if dist_v < d[v]:
                d[v] = dist_v
                heappush(h, (dist_v, v))

INF = 1e9
d = [INF] * (V+1)

dijkstra(K)
for i in range(1, V+1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])