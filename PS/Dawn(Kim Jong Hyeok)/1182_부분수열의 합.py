import sys
def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
combination = []


def solution(start):
    global cnt
    if sum(combination) == s and len(combination) > 0:
        cnt += 1
    for i in range(start, n):
        combination.append(li[i])
        solution(i + 1)
        combination.pop()

solution(0)
print(cnt)