from sys import stdin

stdin = open("input/BOJ_2239_스도쿠.txt")

sudoku = []
for _ in range(9):
    sudoku += list(map(int, stdin.readline().rstrip()))

def check_num(idx):
    row_s = idx-idx%9
    col_s = idx%9
    square_s = (row_s//27)*27+col_s
    area=[]

    for i in range(9):
        area.append(row_s+i)
        area.append(col_s+9*i)
        area.append(square_s+((i//3)*9)+(i%3))
    area_set = list(set(area))
    
    num_list = []
    for n in range(1, 10):
        flag = True
        for a in area_set:
            if sudoku[a] == n:
                flag = False
                break
        if flag:
            num_list.append(n)
    
    return num_list


def dfs(idx):

    if idx == 81:
        for i in range(9):
            print("".join(sudoku[i*9:i*9+8]))
        return
    
    if sudoku[idx] == 0:
        for n in check_num(idx):
            sudoku[idx] = n
            dfs(idx+1)
            sudoku[idx] = 0
    else: dfs(idx+1)


dfs(0)