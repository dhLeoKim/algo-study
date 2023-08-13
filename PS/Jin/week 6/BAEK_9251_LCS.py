text1 = input()
text2 = input()

arr = [[0] * len(text2) for _ in range(len(text1))]

for i in range(len(text1)):
    for j in range(len(text2)):
        if i == 0 or j == 0:
            if text1[i] == text2[j]:
                arr[i][j] = 1
            else:
                if i == 0:
                    arr[i][j] = arr[i][j-1]
                else:
                    arr[i][j] = arr[i-1][j]
        else:
            if text1[i] == text2[j]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[len(text1)-1][len(text2)-1])