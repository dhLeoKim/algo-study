import sys
sys.stdin = open('input_13549.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    global ret

    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.popleft()
        if now == end:
            ret = min(ret, visited[now])
        
        for nxt in (2*now, now-1, now+1):
            if nxt >= 0 and nxt <= 100001 and visited[nxt] == -1:
                queue.append(nxt)
                if nxt == 2*now:
                    visited[nxt] = visited[now]
                else:
                    visited[nxt] = visited[now]+1
    

N, K = map(int, input().split())
visited = [-1]*(100005)
ret = 1e11
bfs(N, K)

print(ret)