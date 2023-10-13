import sys

N = int(input())
dd = [[0, 1], [-1, 0], [0, -1], [1, 0]]
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    # 시작점 y, x (x, y 좌표 반대로) / 시작방향 d / 세대 g
    y, x, d, g = map(int, sys.stdin.readline().strip().split())

    # 방향 표시
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)-1, -1, -1):
            temp.append((move[i] + 1) % 4)
        move.extend(temp)

    # 이동 표시
    arr[x][y] = 1
    for i in move:
        x += dd[i][0]
        y += dd[i][1]
        arr[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            if arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
                cnt += 1

print(cnt)