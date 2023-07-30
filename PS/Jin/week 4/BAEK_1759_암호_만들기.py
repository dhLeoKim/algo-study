# 최소 1개의  모음과  최소 2개의 자음
# 알바펫이 증가

import itertools

L, C = list(map(int, input().split()))
alphabet = sorted(input().split())
# print(alphabet)
vowel = ['a', 'e', 'i', 'o', 'u']

nCr = itertools.combinations(alphabet, L)
# print(list(nCr))

for i in list(nCr):
    code = ''
    v, c = 0, 0
    for j in i:
        if j in vowel:
            v += 1
        else:
            c += 1
        code += j
    if v >= 1 and c >= 2:
        print(code)