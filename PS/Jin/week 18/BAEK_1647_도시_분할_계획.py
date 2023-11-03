import sys
from heapq import heappop, heappush

def prim(start):
    h = []
    MST[start] = 1
    res = []
    for v, w in graph[start]:
        heappush(h, (w, v))

    cnt = 1
    while cnt < N:
        w, v = heappop(h)
        if not MST[v]:
            res.append(w)
            MST[v] = 1
            cnt += 1
            for next_v, next_w in graph[v]:
                if not MST[next_v]:
                    heappush(h, (next_w, next_v))
    return sum(res) - max(res)

N, M = map(int, input().split())
MST = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
print(prim(1))