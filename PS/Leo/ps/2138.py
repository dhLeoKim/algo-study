import sys
sys.stdin = open('input_2138.txt')
input = sys.stdin.readline

def switch(lst, cnt):
    temp = lst[:]
    for i in range(1, N):
        if temp[i-1] == result[i-1]:
            continue
        
        cnt += 1
        for j in range(i-1, i+2):
            if j < N:
                temp[j] = 1-temp[j]

    if temp == result:
        return cnt
    else:
        return -1


N = int(input())
bulb = list(map(int, input().strip()))
result = list(map(int, input().strip()))

# 1번 전구의 스위치를 누르지 않은 경우
cnt_off = switch(bulb, 0)

# 1번 전구의 스위치를 누른 경우
bulb[0] = 1-bulb[0]
bulb[1] = 1-bulb[1]
cnt_on = switch(bulb, 1)

ret = 0
if cnt_off == -1 and cnt_on == -1:
    ret = -1
elif cnt_off == -1 or cnt_on == -1:
    ret = max(cnt_off, cnt_on)
else:
    ret = min(cnt_off, cnt_on)

print(ret)