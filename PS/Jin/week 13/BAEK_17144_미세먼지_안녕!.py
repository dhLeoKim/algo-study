import sys
import copy

R, C, T = map(int, input().split())
# 공기청정기
cir = []
# 집 구조
arr = []
for i in range(R):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    if temp[0] == -1:
        cir.append(i)
    arr.append(temp)
# 방향
dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while T > 0:
    T -= 1

    # 미세먼지 확산
    arr_copy = copy.deepcopy(arr)
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 4:
                for di, dj in dd:
                    if 0 <= i+di < R and 0 <= j+dj < C and arr[i+di][j+dj] != -1:
                        arr_copy[i+di][j+dj] += (arr[i][j] // 5)
                        arr_copy[i][j] -= (arr[i][j] // 5)
    arr = arr_copy

    # 공기청정기 작동

    # 공기청정기 위쪽
    # 아래 방향
    for i in range(cir[0]-1, -1, -1):
        arr[i][0] = arr[i-1][0]
    # 왼쪽 방향
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
    # 위쪽 방향
    for i in range(cir[0]):
        arr[i][C-1] = arr[i+1][C-1]
    # 오른쪽 방향
    for j in range(C-1, 0, -1):
        arr[cir[0]][j] = arr[cir[0]][j-1]
        if j == 1:
            arr[cir[0]][j] = 0

    # 공기청정기 아래쪽
    # 위쪽 방향
    for i in range(cir[1]+1, R-1):
        arr[i][0] = arr[i+1][0]
    # 왼쪽 방향
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
    # 아래 방향
    for i in range(R-1, cir[1], -1):
        arr[i][C-1] = arr[i-1][C-1]
    # 오른쪽 방향
    for j in range(C - 1, 0, -1):
        arr[cir[1]][j] = arr[cir[1]][j - 1]
        if j == 1:
            arr[cir[1]][j] = 0

total = 2       # 공기청정기 제외
for i in range(R):
    total += sum(arr[i])
print(total)