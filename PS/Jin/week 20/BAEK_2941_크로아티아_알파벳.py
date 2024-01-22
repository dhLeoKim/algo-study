import sys

w = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

cnt = 0
while word:
    if word[:3] == 'dz=':
        word = word[3:]
    elif word[:2] in w:
        word = word[2:]
    else:
        word = word[1:]
    cnt += 1
print(cnt)