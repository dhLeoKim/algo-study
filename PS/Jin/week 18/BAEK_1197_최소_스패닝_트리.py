import sys
from heapq import heappop, heappush

def prim(start):
    h = []
    MST[start] = 1
    total = 0
    for v, w in adjList[start]:
        heappush(h, (w, v))

    cnt = 0
    while cnt < V-1:
        w, v = heappop(h)
        if MST[v]:
            continue
        total += w
        MST[v] = 1
        cnt += 1
        for nv, nw in adjList[v]:
            if MST[nv] == 0:
                heappush(h, (nw, nv))
    return total

V, E = map(int, input().split())
adjList = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    adjList[A].append((B, C))
    adjList[B].append((A, C))
MST = [0] * (V+1)
print(prim(1))