import sys
sys.stdin = open('input_17609.txt')
input = sys.stdin.readline

def chkPalindrome(start, end):
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
        
    return True


T = int(input())
for _ in range(T):
    string = input().strip()
    L = len(string)
    start = 0
    end = L-1
    ret = 0

    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            chk1 = chkPalindrome(start+1, end)
            chk2 = chkPalindrome(start, end-1)

            if chk1 or chk2:
                ret = 1
                break
            else:
                ret = 2
                break

    print(ret)