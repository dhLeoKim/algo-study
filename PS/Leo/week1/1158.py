import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

lst = deque([str(i) for i in range(1, N+1)])

ret = []
while lst:
    lst.rotate(-K)
    ret.append(lst.pop())

print('<' + ', '.join(ret) + '>')