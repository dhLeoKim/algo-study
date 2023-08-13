import sys
sys.stdin = open('input_2206.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    