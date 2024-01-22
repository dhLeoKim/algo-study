import sys
from heapq import heappush, heappop

def dijkstra(start):
    h = []
    cnt = 0
    d[start][cnt] = 0
    heappush(h, (0, start, cnt))
    while h:
        dist_u, u, cnt = heappop(h)
        if dist_u > d[u][cnt]:
            continue
        for v, w in graph[u]:
            dist_v = dist_u + w
            # 그냥 다익스트라
            if dist_v < d[v][cnt]:
                d[v][cnt] = dist_v
                heappush(h, (dist_v, v, cnt))
            # 포장하는 다익스트라
            if cnt < K and d[v][cnt+1] > dist_u:
                d[v][cnt+1] = dist_u
                heappush(h, (dist_u, v, cnt+1))


N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
d = [[10e9 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
dijkstra(1)
print(min(d[N]))