import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
X = int(input())

ret = 0
numbers = [0]*1000001
for number in lst:
    numbers[number] = 1
    print(X-number)
    if X-number <= 1000000 and numbers[X-number] and number*2 != X and number != X:
        ret += 1

print(ret)