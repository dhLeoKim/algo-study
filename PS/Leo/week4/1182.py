import sys
sys.stdin = open('input_1182.txt')
input = sys.stdin.readline

def subset(k, total):
    global ret
    
    if k == N:
        if total == S:
            ret += 1
        return
    
    subset(k+1, total)
    subset(k+1, total+lst[k])


N, S = map(int, input().split())
lst = list(map(int, input().split()))

ret = 0
subset(0, 0)

if S == 0:
    print(ret-1)
else:
    print(ret)