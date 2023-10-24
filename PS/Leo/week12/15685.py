import sys
sys.stdin = open('input_15685.txt')
input = sys.stdin.readline

# 1. 기준점에서 원점으로만큼 평행이동 : p-a, q-b
# 2. 원점에서 시계방향 90도 회전      : -q+b, p-a 
# 3. 다시 원래대로 평행이동           : -q+b+a, p-a+b

def genDragonCurve(g, depth):
    while depth < g:
        b, a = dragonCurve[-1]
        for i in range(len(dragonCurve)-2, -1, -1):
            q, p = dragonCurve[i]
            nq, np = p-a+b, -q+b+a
            dragonCurve.append((nq, np))
            grid[nq][np] = 1
        
        depth += 1
            

grid = [[0]*101 for _ in range(101)]
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    depth = 0
    dragonCurve = [(y, x), (y+dy[d], x+dx[d])]
    grid[y][x] = 1
    grid[y+dy[d]][x+dx[d]] = 1

    genDragonCurve(g, depth)

ret = 0
for i in range(100):
    for j in range(100):
        chk = grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]
        if chk == 4:
            ret += 1

print(ret)