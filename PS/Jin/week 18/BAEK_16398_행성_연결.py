import sys
from heapq import heappop, heappush

def prim(start):
    h = []
    MST[start] = 1
    res = 0
    for c in range(N):
        if arr[start][c] != 0:
            heappush(h, (arr[start][c], c))

    cnt = 1
    while cnt < N:
        w, v = heappop(h)
        if not MST[v]:
            res += w
            MST[v] = 1
            cnt += 1
            for c in range(N):
                if not MST[c] and arr[v][c] != 0:
                    heappush(h, (arr[v][c], c))
    return res

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
MST = [0] * (N+1)
print(prim(0))