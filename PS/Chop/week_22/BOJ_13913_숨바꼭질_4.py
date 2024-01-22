from sys import stdin
from collections import deque

stdin = open("input/BOJ_13913_숨바꼭질_4.txt")

x, k = map(int, stdin.readline().split())
ans = [k]

def bfs():
    q = deque([[k]])

    while q:
        now = q.popleft()
        # print(now)
        if now[-1] == x: return now
        
        if now[-1] % 2 == 0:
            now.append(now[-1] / 2)
            q.append(now)
        else:
            for i in [1, -1]:
                now.append(now[-1] + i)
                q.append(now)
                print(q)
                now.pop()



if x >= k: print(x - k)
else: print(bfs())