from sys import stdin

stdin = open("input/BOJ_2457_공주님의_정원.txt")

N = int(stdin.readline().rstrip())
arr = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

# 날짜 대소 비교를 위해 월,일을 숫자로 변환 ex) 1월 1일 > 101
flowers = [[x[0]*100+x[1], x[2]*100+x[3]] for x in arr]
flowers.sort(key=lambda x: x[0])

def count_flowers():
    period = [101, 301]
    idx, cnt = 0, 0

    while period[1] <= 1130:
        temp_end = period[0]
        for i in range(idx, N):
        
            if period[0] <= flowers[i][0] <= period[1]:
                if flowers[i][1] > 1130:
                    cnt += 1
                    return cnt
                if flowers[i][1] >= temp_end:
                    temp_end = flowers[i][1]
                idx = i+1
            else:
                break
                
        if temp_end <= period[1]:
            return 0
        else:
            cnt += 1
            period = [period[1], temp_end]

    return cnt

print(count_flowers())