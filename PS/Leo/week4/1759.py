import sys
sys.stdin = open('input_1759.txt')
input = sys.stdin.readline

def chkPassword(idx, pw):
    if len(pw) == L:
        vowel_cnt, consonant_cnt = 0, 0

        for chr in pw:
            if chr in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(pw))

        return
    
    if idx == C:
        return

    pw.append(lst[idx])
    chkPassword(idx+1, pw)
    pw.pop()
    chkPassword(idx+1, pw)


L, C = map(int, input().split())
lst = list(input().split())

lst.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
pw = []
chkPassword(0, pw)