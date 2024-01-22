from sys import stdin
from itertools import combinations
from collections import deque

stdin = open("input/BOJ_17471_게리맨더링.txt")

N = int(stdin.readline())
pp = [0] +  list(map(int, stdin.readline().rstrip().split()))
total = sum(pp)
graph = [[0]] + [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
res = 1e5
print(graph)

def bfs(comb):
    start = comb[0]
    q = deque([start])
    visited = set([start])
    sum_pp = 0
    while q:
        now = q.popleft()
        sum_pp += pp[now]
        for next in graph[now][1:]:
            if next not in visited and next in comb:
                q.append(next)
                visited.add(next)
    return sum_pp

for i in range(1, N//2 + 1):
    combs = list(combinations(range(N), i))
    for comb in combs:
        sum1, sum2 = bfs(comb), bfs([i for i in range(N) if i not in comb])
        if sum1 + sum2 == total:
            res = min(res, abs(sum1 - sum2))

if res != 1e5: print(res)
else: print(-1)