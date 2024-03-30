import sys
sys.stdin = open('input_1976.txt')
input = sys.stdin.readline

def find(x):
    if p[x] < 0:
        return x
    return find(p[x])


def union(u, v):
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:
        p[pu] -= 1
    if p[pu] < p[pv]:
        p[pv] = pu
    else:
        p[pu] = pv


N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
p = [-1]*N
for i in range(N):
    for j in range(i+1, N):
        if lst[i][j] == 1 and find(i) != find(j):
            union(i, j)

chk_pass = list(map(int, input().split()))
chk_city = find(chk_pass[0]-1)
for i in range(len(chk_pass)):
    if find(chk_pass[i]-1) != chk_city:
        print('NO')
        break
else:
    print('YES')