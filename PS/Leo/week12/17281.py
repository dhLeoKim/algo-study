import sys
sys.stdin = open('input_17281.txt')
input = sys.stdin.readline

def dfs(k, order):
    global ret

    if k == 8:      
        order = order[:3] + [0] + order[3:]             # 타순 경우의 수 생성 완료
        num = 0
        score = 0
        for inning in range(N):
            temp, num = calScore(inning, order, num)    # 해당 타순의 점수 계산
            score += temp
        ret = max(ret, score)                           # 최대값 갱신
        return 

    for i in range(1, 9):                               # 순열 8P7 = 8! 생성
        if i not in order:
            order.append(i)
            dfs(k+1, order)
            order.pop()


def calScore(inning, order, num):
    out_cnt = 0   
    temp = lst[inning]
    batter = [0]*9
    for i in range(9):
        batter[i] = temp[order[i]]                      # 타자 결과 저장

    base = [0, 0, 0, 0]
    while out_cnt < 3:                                  # 득점 계산
        if batter[num] == 0:
            out_cnt += 1
        elif batter[num] == 1:
            base[0] += base[3]
            base[3] = base[2]
            base[2] = base[1]
            base[1] = 1
        elif batter[num] == 2:
            base[0] += base[3] + base[2]
            base[3] = base[1]
            base[2] = 1
            base[1] = 0
        elif batter[num] == 3:
            base[0] += base[3] + base[2] + base[1]
            base[3] = 1
            base[2] = 0
            base[1] = 0
        elif batter[num] == 4:
            base[0] += base[3] + base[2] + base[1] + 1
            base[3] = 0
            base[2] = 0
            base[1] = 0

        num = (num+1)%9

    return base[0], num


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ret = 0
dfs(0, [])
print(ret)