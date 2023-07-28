from sys import stdin

stdin = open("input/BAEK_1759_암호_만들기.txt")

l, n = map(int, stdin.readline().rstrip().split())
c = sorted(list(stdin.readline().rstrip().split()))

def dfs(step, total):
    if len(total) == l:
        aeiou = 0
        for i in total:
            if i in 'aeiou':
                aeiou += 1
        if aeiou >= 1 and len(total) - aeiou >=2:
            print(total)
        return
    if step == n:
        return

    dfs(step + 1, total+c[step])
    dfs(step + 1, total)

dfs(0, '')