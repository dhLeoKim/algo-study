import sys
sys.stdin = open('input_5972.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))

    while h:
        now_w, now = heappop(h)
        if now_w > d[now]:
            continue
        for nxt, w in graph[now]:
            nxt_w = now_w + w
            if nxt_w < d[nxt]:
                heappush(h, (nxt_w, nxt))
                d[nxt] = nxt_w


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = 1e11
d = [INF]*(N+1)

dijkstra(1)

print(d[N])