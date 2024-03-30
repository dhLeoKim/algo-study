import sys
sys.stdin = open('input_1253.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

ret = 0
for i in range(N):
    chk_good = lst[i]
    start = 0
    end = len(lst)-1
    while start < end:
        if lst[start] + lst[end] == chk_good:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                ret += 1
                break
        elif lst[start] + lst[end] > chk_good:
            end -= 1
        elif lst[start] + lst[end] < chk_good:
            start += 1

print(ret)