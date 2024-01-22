import sys
from heapq import heappop, heappush

def prim(start):
    global total
    h = []
    heappush(h, (0, start))
    while h:
        w, v = heappop(h)
        if MST[v]:
            continue
        MST[v] = 1
        total += w
        for i in range(1, N+1):
            if MST[i] == 0:
                heappush(h, (adjList[i][v], i))


N, M = map(int, input().split())
nodes = [(-1, -1)]
adjList = [[0 for _ in range(N+1)] for _ in range(N+1)]
MST = [0] * (N+1)
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().strip().split())
    nodes.append((X, Y))
for i in range(1, N+1):
    for j in range(1, N+1):
        adjList[i][j] = ((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2) ** (1/2)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    adjList[a][b] = 0
    adjList[b][a] = 0
total = 0
prim(1)
print(f"{total:.2f}")