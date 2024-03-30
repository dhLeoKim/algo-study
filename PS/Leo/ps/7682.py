import sys
sys.stdin = open('input_7682.txt')
input = sys.stdin.readline

def chkBoard():
    if (
        (board[0][0] == board[0][1] == board[0][2] and board[0][0] != '.') or 
        (board[1][0] == board[1][1] == board[1][2] and board[1][0] != '.') or 
        (board[2][0] == board[2][1] == board[2][2] and board[2][0] != '.') or 
        (board[0][0] == board[1][0] == board[2][0] and board[0][0] != '.') or 
        (board[0][1] == board[1][1] == board[2][1] and board[0][1] != '.') or 
        (board[0][2] == board[1][2] == board[2][2] and board[0][2] != '.') or 
        (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.') or 
        (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.')
       ):
        return True
    
    return False


def dfs(turn, now):
    if turn == 10 or chkBoard():
        temp = ''
        for row in board:
            temp += ''.join(row)

        valid_case.add(temp)
        return

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X' if now == 1 else 'O'
                dfs(turn+1, -1*now)
                board[i][j] = '.'


board = [['.']*3 for _ in range(3)]
valid_case = set()

dfs(1, 1)

while True:
    tc = input().strip()
    if tc == 'end':
        break

    print('valid' if tc in valid_case else 'invalid')



# 다른 풀이 : 가능한 경우의 수를 나눠서 판단

# 1. X가 이기는 경우, O보다 한칸 더 많아야 함
# 2. O가 이기는 경우, O와 X의 수는 같아야 함
# 3. 무승부인 경우, X는 5개 O는 4개로 가득참
# 4. 나머지, 발생할 수 없는 경우