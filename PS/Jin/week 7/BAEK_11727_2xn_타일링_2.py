n = int(input())
tiles = [0] * 1001
tiles[0] = 1
tiles[1] = 1

for i in range(2, 1001):
    tiles[i] = tiles[i-1] + 2*tiles[i-2]

print(tiles[n] % 10007)