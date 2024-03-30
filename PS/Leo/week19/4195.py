import sys
sys.stdin = open('input_4195.txt')
input = sys.stdin.readline

from collections import defaultdict

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
        f[pu] += f[pv]
    else:
        p[pu] = pv
        f[pv] += f[pu]


tc = int(input())
for case in range(tc):
    
    F = int(input())
    p = [-1]*(100001)
    f = [1]*(100001)
    user_id = defaultdict(int)
    user_num = 1

    for _ in range(F):
        a, b = input().strip().split()
        if user_id[a] == 0:
            user_id[a] = user_num
            user_num += 1
        if user_id[b] == 0:
            user_id[b] = user_num
            user_num += 1
        
        u = user_id[a]
        v = user_id[b]
        if find(u) != find(v):
            union(u, v)
        
        pu = find(u)
        pv = find(v)

        print(f[pu])