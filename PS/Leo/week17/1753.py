import sys
sys.stdin = open('input_1753.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(now):
    h = []
    d[now] = 0
    heappush(h, (0, now))

    while h:
        dist, now = heappop(h)
        if d[now] < dist:
            continue
        for nxt, w in graph[now]:
            ndist = dist + w
            if ndist < d[nxt]:
                d[nxt] = ndist
                heappush(h, (ndist, nxt))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 1e9
d = [INF]*(V+1)
d[0] = 0

dijkstra(start)
for i in range(1, V+1):
    print('INF' if d[i] == INF else d[i])