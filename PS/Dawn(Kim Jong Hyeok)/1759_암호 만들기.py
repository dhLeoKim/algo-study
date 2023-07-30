import sys
def input():
    return sys.stdin.readline().rstrip()

l, c = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
answer=[]
# print(alphabet)
def find_possibillty(idx):
    if len(answer) == l:
        vowel, consonant = 0, 0

        for i in answer:
            if i in ['a','e','i','o','u']:
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            print("".join(answer))
        return

    for i in range(idx, c):
        answer.append(alphabet[i])
        find_possibillty(i+1)
        answer.pop()



find_possibillty(0)
