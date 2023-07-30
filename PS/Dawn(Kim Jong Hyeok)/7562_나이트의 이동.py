import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

tc = int(input())
for t in range(tc):
    l = int(input())
    now = list(map(int, input().split()))
    final = list(map(int, input().split()))
    graph = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]

    q = deque()

    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    def bfs():
        q.append(now)
        visited[now[0]][now[1]] = 1

        while q:
            r,c = q.popleft()

            if r == final[0] and c == final[1]:
                return 0
            
            for k in range(8):
                nr = r + dr[k] 
                nc = c + dc[k]    

                if nr < 0 or nr >= l or nc < 0 or nc >= l:
                    continue

                if nr == final[0] and nc == final[1]:
                    visited[nr][nc] = 1
                    return graph[r][c] + 1
                
                if visited[nr][nc] == 0:
                    q.append([nr,nc])
                    visited[nr][nc] = 1
                    graph[nr][nc] = graph[r][c] + 1

    print(bfs()) 

