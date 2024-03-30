import sys
sys.stdin = open('input_1316.txt')
input = sys.stdin.readline

N = int(input())
ret = 0
for _ in range(N):
    word = input().strip()
    chk = [False]*27
    temp = word[0]
    for char in word:
        idx = ord(char)-97
        if temp != char:
            if not chk[idx]:
                chk[idx] = True
                temp = char
            else:
                break
        elif temp == char:
            chk[idx] = True
    else:
        ret += 1

print(ret)