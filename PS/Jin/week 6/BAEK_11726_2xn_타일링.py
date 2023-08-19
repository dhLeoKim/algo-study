n = int(input())
tiles = [0] * (n+1)

def tile(n):
    if tiles[n]:
        pass
    elif n == 1:
        tiles[1] = 1
    elif n == 2:
        tiles[2] = 2
    else:
        tiles[n] = tile(n-1) + tile(n-2)
    return tiles[n]

answer = tile(n) % 10007
print(answer)