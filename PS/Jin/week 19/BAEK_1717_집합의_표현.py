import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
p = [i for i in range(n+1)]

# union-find
def find(x):                                    # 부모 찾기
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(u, v):                                # 합치기
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:                          # 랭크가 같다면 한쪽을 -1
        p[pu] -= 1
    if p[pu] < p[pv]:                           # 랭크가 낮은 쪽으로 합치기
        p[pv] = pu
    else:
        p[pu] = pv

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().strip().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")