N, r, c = list(map(int, input().split()))
count = 0

while N > 0:
    if r < 2**(N-1):
        if c < 2**(N-1):
            pass
        else:
            c -= 2**(N-1)
            count += (2**(N-1))**2
    else:
        r -= 2**(N-1)
        if c < 2**(N-1):
            count += 2 * (2**(N-1))**2
        else:
            c -= 2**(N-1)
            count += 3 * (2**(N-1))**2
    N -= 1
print(count)