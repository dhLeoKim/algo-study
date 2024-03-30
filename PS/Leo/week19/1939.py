import sys
sys.stdin = open('input_1939.txt')
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


N, M = map(int, input().split())
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort(reverse=True)

s, e = map(int, input().split())

p = [-1]*(N+1)
# ret = 1e9 사용시 통과x (1e9는 float, 1000000000은 int)
# 최대값이 1e9 이기 때문에 초기값을 그보다 큰 값(1e11)으로 설정해야 됨!!
ret = 10000000000          
for c, a, b in edge:
    if find(a) != find(b):
        union(a, b)
    ret = min(ret, c)
    if find(s) == find(e):
        break

print(ret)