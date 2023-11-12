import sys
from itertools import combinations
from collections import deque

N = int(input())
po = list(map(int, input().split()))
adjList = [[]]
res = 10e9
for _ in range(N):
    info = list(map(int, input().split()))
    if info:
        adjList.append(info[1:])
    else:
        adjList.append([])

def bfs(reg):
    total = 0
    cnt = 0
    q = deque()
    q.append(reg[0])
    visited[reg[0]] = 1
    while q:
        r = q.popleft()
        total += po[r-1]
        cnt += 1
        for i in adjList[r]:
            if i in reg and not visited[i]:
                visited[i] = 1
                q.append(i)
    else:
        if len(reg) == cnt:
            return total
        else:
            return False

num = [i for i in range(1, N+1)]
# 한 구역의 수 정하기 (절반 이하로, 나머지인 절반 이상은 reg2로 정해줌)
for i in range(1, N//2 + 1):
    # i개의 구역 정하기
    com = list(combinations(num, i))
    for j in range(len(com)):
        reg1 = list(com[j])
        # reg2는 N-i개의 구역
        reg2 = []
        for k in range(1, N+1):
            if k not in reg1:
                reg2.append(k)
        visited = [0] * (N+1)
        res1 = bfs(reg1)
        res2 = bfs(reg2)
        if res1 and res2:
            res = min(res, abs(res1 - res2))
if res == 10e9:
    print(-1)
else:
    print(res)