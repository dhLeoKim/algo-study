file = open("input/BAEK_3273_두_수의_합.txt")
n = int(file.readline().strip())
num_arr = sorted(list(map(int, file.readline().strip().split())), reverse=True)
x = int(file.readline().strip())
ans = 0

i, j = 0, n-1

while i < j:
    # 투포인터 알고리즘 사용
    temp = num_arr[i] + num_arr[j]
    if temp == x:
        ans += 1
        i += 1
        j -= 1
    elif temp < x:
        i += 1
    else:
        j -= 1

print(ans)
