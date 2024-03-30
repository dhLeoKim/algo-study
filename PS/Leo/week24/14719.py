import sys
sys.stdin = open('input_14719.txt')
input = sys.stdin.readline

H, W = map(int, input().split())
lst = list(map(int, input().split()))

ret = 0
for i in range(1, W-1):
    left = max(lst[:i])
    right = max(lst[i+1:])
    temp = min(left, right)

    if lst[i] < temp:
        ret += temp-lst[i]

print(ret)