from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

dz = [0,0,0,0,-1,1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]

def bfs():
    q = deque()
    q.append([start_z,start_x,start_y])
    visited[start_z][start_x][start_y] = 1
    while q:
        z,x,y = q.popleft()
        for k in range(6):
            nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
                if maps[nz][nx][ny] == '.' or maps[nz][nx][ny] == 'E':
                    escape[nz][nx][ny] = escape[z][x][y] + 1
                    q.append([nz,nx,ny])
                    visited[nz][nx][ny] = 1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0 : 
        break
    else:
        maps = [[] * R for _ in range(L)]
        escape = [[[0] * C for _ in range(R)] for _ in range(L)]
        visited = [[[0] * C for _ in range(R)] for _ in range(L)]
        for i in range(L):
            for j in range(R):
                maps[i].append(list(map(str,input())))
            input()
            
        for k in range(L):
            for i in range(R):
                for j in range(C):
                    if maps[k][i][j] == 'S':
                        start_z,start_x,start_y = k,i,j
                    elif maps[k][i][j] == 'E':
                        end_z,end_x,end_y = k,i,j
        bfs()
        if escape[end_z][end_x][end_x]:
            print("Escaped in " + str(escape[end_z][end_x][end_y]) + " minute(s).")
        else:
            print("Trapped!")