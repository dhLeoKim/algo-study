import sys
sys.stdin = open('input_13913.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    p[start] = start

    while queue:
        now, time = queue.popleft()

        if now == K:
            path = []
            while p[now] != now:
                path.append(now)
                now = p[now]
            path.append(now)
            return time, path
        
        for nxt in (now-1, now+1, now*2):
            if 0 <= nxt < 100001 and p[nxt] == -1:
                queue.append((nxt, time+1))
                p[nxt] = now


N, K = map(int, input().split())

p = [-1]*100001

time, path = bfs(N)

print(time)
print(*path[::-1])