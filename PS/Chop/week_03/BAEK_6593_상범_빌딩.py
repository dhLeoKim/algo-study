from sys import stdin
from collections import deque
stdin = open("input/BAEK_6593_상범_빌딩.txt")

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS():
    q = deque([(sx, sy, sz)])
    building[sz][sy][sx] = 0

    while q:
        (x, y, z) = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if building[nz][ny][nx] == ".":
                    building[nz][ny][nx] = building[z][y][x] + 1
                    q.append((nx, ny, nz))
                elif building[nz][ny][nx] == "E":
                    print(f"Escaped in {building[z][y][x] + 1} minute(s).")
                    return
    print("Trapped!")

while True:
    L, R, C = map(int, stdin.readline().rstrip().split())
    if (L, R, C) == (0, 0, 0):
        break

    building = []
    s_found = False
    for i in range(L):
        floor = []
        for j in range(R):
            line = list(stdin.readline().rstrip())
            floor.append(line)
            if s_found == False:
                for k in range(C):
                    if line[k] == "S":
                        sx, sy, sz = k, j, i
        stdin.readline()
        building.append(floor)
    BFS()