import sys

N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    word = word.lower()
    chk = []
    for i in range(len(word)):
        if chk:
            if word[i] not in chk:
                chk.append(word[i])
            elif word[i] != chk[-1]:
                break
        else:
            chk.append(word[i])
    else:
        cnt += 1
print(cnt)