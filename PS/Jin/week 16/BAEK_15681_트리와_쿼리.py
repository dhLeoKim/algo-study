import sys
sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().split())
adjList = [[] for _ in range(N+1)]
cnt = [0] * (N+1)
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().strip().split())
    adjList[u].append(v)
    adjList[v].append(u)

def countPoint(x):
    cnt[x] = 1
    for i in adjList[x]:
        if not cnt[i]:
            countPoint(i)
            cnt[x] += cnt[i]

countPoint(R)

for i in range(Q):
    u = int(sys.stdin.readline().strip())
    print(cnt[u])