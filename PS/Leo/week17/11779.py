import sys
sys.stdin = open('input_11779.txt')
input = sys.stdin.readline

from heapq import heappop, heappush

def dijsktra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    
    while h:
        dist, now = heappop(h)
        if d[now] < dist:
            continue
        for nxt, w in graph[now]:
            ndist = dist + w
            if ndist < d[nxt]:
                d[nxt] = ndist
                heappush(h, (ndist, nxt))
                pre[nxt] = now


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

S, E = map(int, input().split())

INF = 1e9
d = [INF]*(N+1)
pre = [0]*(N+1)

dijsktra(S)
print(d[E])

now = E
ret = []
while now != 0:
    ret.append(now)
    now = pre[now]

print(len(ret))
print(*ret[::-1])