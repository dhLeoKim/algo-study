import sys
sys.stdin = open('input_2239.txt')
input = sys.stdin.readline

def chkNumber(i, j):
    num_lst = []
    for num in range(1, 10):
        if cnt_row[i][num-1] == 0 and cnt_col[j][num-1] == 0 and cnt_sqr[3*(i//3) + j//3][num-1] == 0:
            num_lst.append(num)

    return num_lst


def dfs(idx):
    i, j = idx//9, idx%9

    if idx == 81:
        for i in range(9):
            print(*lst[i], sep='')
        exit()

    if lst[i][j] == 0:
        num_lst = chkNumber(i, j)
        for num in num_lst:        
            # 방문표시
            lst[i][j] = num
            cnt_row[i][num-1] = 1
            cnt_col[j][num-1] = 1
            cnt_sqr[3*(i//3) + j//3][num-1] = 1
            dfs(idx+1)
            # 방문표시제거
            lst[i][j] = 0
            cnt_row[i][num-1] = 0
            cnt_col[j][num-1] = 0
            cnt_sqr[3*(i//3) + j//3][num-1] = 0
    else:
        dfs(idx+1)


lst = [list(map(int, input().strip())) for _ in range(9)]
cnt_row = [[0]*9 for _ in range(9)]     # 가로
cnt_col = [[0]*9 for _ in range(9)]     # 세로
cnt_sqr = [[0]*9 for _ in range(9)]     # 3x3 사각형

for i in range(9):
    for j in range(9):
        if lst[i][j] != 0:
            cnt_row[i][lst[i][j]-1] = 1
            cnt_col[j][lst[i][j]-1] = 1
            cnt_sqr[3*(i//3) + j//3][lst[i][j]-1] = 1

dfs(0)