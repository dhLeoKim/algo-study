import sys

A, B = list(input().split())
minC = 10e9
for i in range(len(B) - len(A) + 1):
    temp = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            temp += 1
    else:
        minC = min(minC, temp)

print(minC)