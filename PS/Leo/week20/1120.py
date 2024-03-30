import sys
sys.stdin = open('input_1120.txt')
input = sys.stdin.readline

A, B = input().strip().split()

diff = len(B)-len(A)
ret = 9999
for k in range(diff+1):
    temp = 0
    for i in range(len(A)):
        if A[i] != B[i+k]:
            temp += 1
    
    ret = min(ret, temp)

print(ret)