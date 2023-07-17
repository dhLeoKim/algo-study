import sys
sys.stdin = open('input_6593.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    l, r, c = start
    queue = deque()
    queue.append((l, r, c, 0))

    dl, dr, dc = [1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0 ,0, -1]

    while queue:
        l, r, c, x = queue.popleft()
        for k in range(6):
            nl, nr, nc = l+dl[k], r+dr[k], c+dc[k]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == '.':
                   queue.append((nl, nr, nc, x+1))
                   building[nl][nr][nc] = 'x'
                elif building[nl][nr][nc] == 'E':
                    return f'Escaped in {x+1} minute(s).'

    return 'Trapped!'


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    for l in range(L):
        floor = []
        for r in range(R+1):
            row = list(input().strip())
            if not row:
                continue
            floor.append(row)
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)

        building.append(floor)

    ret = bfs(start)
    print(ret)
