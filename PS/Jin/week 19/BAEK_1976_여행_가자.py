import sys
sys.setrecursionlimit(10**6)

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

N = int(input())
M = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
p = [i for i in range(N)]

# 길이 연결되어 있으면 union
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i, j)

cities = list(map(int, input().split()))
pp = []
for i in cities:
    pp.append(find(i-1))
if len(set(pp)) == 1:
    print("YES")
else:
    print("NO")