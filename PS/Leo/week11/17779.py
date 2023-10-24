import sys
sys.stdin = open('input_17779.txt')
input = sys.stdin.readline

def calc(x, y, d1, d2):
    elec = [0 for _ in range(5)]
    temp = [[0]*N for _ in range(N)]

    # 2번 조건
    for i in range(d1+1):
        temp[x+i][y-i] = 5          # 2-1
        temp[x+d2+i][y+d2-i] = 5    # 2-3
    for i in range(d2+1):
        temp[x+i][y+i] = 5          # 2-2
        temp[x+d1+i][y-d1+i] = 5    # 2-4

    # 3번 조건
    for i in range(x+1, x+d1+d2):   
        flag = False
        for j in range(N):
            if temp[i][j] == 5:
                flag = not flag
            if flag:
                temp[i][j] = 5
    
    for i in range(N):
        for j in range(N):
            if i < x+d1 and j <= y and temp[i][j] == 0:
                elec[0] += lst[i][j]
            elif i <= x+d2 and j > y and temp[i][j] == 0:
                elec[1] += lst[i][j]
            elif i >= x+d1 and j < y-d1+d2 and temp[i][j] == 0:
                elec[2] += lst[i][j]
            elif i > x+d2 and j >= y-d1+d2 and temp[i][j] == 0:
                elec[3] += lst[i][j]
            elif temp[i][j] == 5:
                elec[4] += lst[i][j]
    
    return max(elec) - min(elec)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ret = 1e9

for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                if 0 <= x < x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:   # 1번 조건
                    ret = min(ret, calc(x, y, d1, d2))

print(ret)