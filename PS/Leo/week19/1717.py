import sys
sys.stdin = open('input_1717.txt')
input = sys.stdin.readline

def find(x):
    if p[x] < 0:
        return x
    return find(p[x])


def union(a, b):
    pu = find(a)
    pv = find(b)
    if p[pu] == p[pv]:
        p[pu] -= 1
    if p[pu] < p[pv]:
        p[pv] = pu
    else:
        p[pu] = pv


N, M = map(int, input().split())
p = [-1]*(N+1)
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 1:
        print("YES" if find(a) == find(b) else "NO")
    elif find(a) != find(b):
        union(a, b)