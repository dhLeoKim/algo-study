import sys
sys.stdin = open('input_2457.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key= lambda x: (x[0], x[1]))

sm, sd = 3, 1
em, ed = 0, 0

cnt = 0
i = 0
while em < 12 and i < N:
    if lst[i][0] < sm or (lst[i][0] == sm and lst[i][1] <= sd):     # 피는 날짜가 더 빠를 때
        if lst[i][2] > em or (lst[i][2] == em and lst[i][3] > ed):  # 지는 날짜가 더 늦을 때
            em = lst[i][2]
            ed = lst[i][3]
        
        i += 1
        continue
    elif sm == em and sd == ed:
        break
    else:
        sm = em
        sd = ed
        cnt += 1

if em >= 12:
    cnt += 1
elif i <= N and em < 12:
    cnt = 0

print(cnt)