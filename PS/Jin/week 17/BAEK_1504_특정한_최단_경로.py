import sys
from heapq import heappush, heappop

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())

# 1번 정점에서 N번 정점
def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    while h:
        dist_u, u = heappop(h)
        if dist_u > d[u]:
            continue
        for v, w in graph[u]:
            dist_v = dist_u + w
            if dist_v < d[v]:
                d[v] = dist_v
                heappush(h, (dist_v, v))

temp1 = 0
# case1: 1 -> v1 -> v2 -> N
d = [10e9] * (N+1)
dijkstra(1)
temp1 += d[v1]

d = [10e9] * (N+1)
dijkstra(v1)
temp1 += d[v2]

d = [10e9] * (N+1)
dijkstra(v2)
temp1 += d[N]

temp2 = 0
# case2: 1 -> v2 -> v1 -> N
d = [10e9] * (N+1)
dijkstra(1)
temp2 += d[v2]

d = [10e9] * (N+1)
dijkstra(v2)
temp2 += d[v1]

d = [10e9] * (N+1)
dijkstra(v1)
temp2 += d[N]

if min(temp1, temp2) >= 10e9:
    print(-1)
else:
    print(min(temp1, temp2))