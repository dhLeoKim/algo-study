import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    word = list(sys.stdin.readline().strip())
    # print(word)

    def chk(left, right, word):
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return 0
        else:
            return 1

    # 1. 회문인지 여부
    if word == word[::-1]:
        print(0)
    # 2. 유사 회문인지 여부
    else:
        # 투포인터
        s, e = 0, len(word)-1
        while s < e:
            if word[s] != word[e]:
                if chk(s+1, e, word) or chk(s, e-1, word):
                    print(1)
                else:
                    print(2)
                break
            else:
                s += 1
                e -= 1