import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

lst = list(map(int, input().strip()))
cnt = [0]*10
for number in lst:
    if number == 6 or number == 9:
        cnt[6] += 1
    else:
        cnt[number] += 1

cnt[6] = sum(divmod(cnt[6], 2))
result = max(cnt)

print(result)