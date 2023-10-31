import sys
sys.stdin = open('input_1504.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(now, d):
    h = []
    d[now] = 0
    heappush(h, (0, now))

    while h:
        dist, now = heappop(h)
        if dist > d[now]:
            continue

        for nxt, w in graph[now]:
            ndist = dist + w
            if ndist < d[nxt]:
                d[nxt] = ndist
                heappush(h, (ndist, nxt))


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = 1E9
d1 = [INF]*(N+1)
d2 = [INF]*(N+1)
d3 = [INF]*(N+1)

dijkstra(1, d1)
dijkstra(v1, d2)
dijkstra(v2, d3)

ret = min(d1[v1]+d2[v2]+d3[N], d1[v2]+d3[v1]+d2[N])
print(ret if ret < INF else -1)