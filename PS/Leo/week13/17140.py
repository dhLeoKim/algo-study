import sys
sys.stdin = open('input_17140.txt')
input = sys.stdin.readline

from collections import defaultdict

def dfs(t, R, C):
    global A, ret

    if r <= R and c <= C and A[r-1][c-1] == k:
        ret = t
        return

    if t > 100:
        ret = -1
        return

    if R >= C:                                              # R연산
        temp = []
        temp_max = 0
        for i in range(R):                                  # 숫자 나온횟수세기
            cnt_dict = defaultdict(int)
            for j in range(C):
                num = A[i][j]
                if num == 0:
                    continue

                if cnt_dict[num]:
                    cnt_dict[num] += 1
                else:
                    cnt_dict[num] = 1

            temp_row = list(cnt_dict.items())               # 정렬
            temp_row.sort(key=lambda x : (x[1], x[0]))
            temp.append(temp_row)
            temp_max = max(temp_max, len(temp_row))

        C = max(3, temp_max*2)
        A = [[0]*C for _ in range(R)]                       # 새로운 A row 순서로 갱신
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                A[i][2*j] = temp[i][j][0]
                A[i][2*j+1] = temp[i][j][1]

    else:                                                   # C연산
        temp = []
        temp_max = 0
        for j in range(C):                                  # 숫자 나온횟수세기
            cnt_dict = defaultdict(int)
            for i in range(R):
                num = A[i][j]
                if num == 0:
                    continue

                if cnt_dict[num]:
                    cnt_dict[num] += 1
                else:
                    cnt_dict[num] = 1

            temp_row = list(cnt_dict.items())               # 정렬
            temp_row.sort(key=lambda x : (x[1], x[0]))
            temp.append(temp_row)
            temp_max = max(temp_max, len(temp_row))

        R = max(3, temp_max*2)
        A = [[0]*C for _ in range(R)]                       # 새로운 A col 순서로 갱신
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                A[2*j][i] = temp[i][j][0]
                A[2*j+1][i] = temp[i][j][1]

    dfs(t+1, R, C)


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

R, C = 3, 3
ret = 0
dfs(0, R, C)

print(ret)