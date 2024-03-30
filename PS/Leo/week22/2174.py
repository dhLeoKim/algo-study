import sys
sys.stdin = open('input_2174.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

board = [[0]*A for _ in range(B)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
direction_dict = {'E': 0, 'S': 1, 'W':2, 'N': 3}
robot_num = 1
robot = [[]]
for _ in range(N):
    x, y, k = input().strip().split()
    i, j = B-int(y), int(x)-1
    board[i][j] = robot_num
    robot_num += 1
    robot.append([i, j, direction_dict[k]])

ret = 'OK'
flag = False
for _ in range(M):
    robot_num, command, cnt = input().strip().split()
    robot_num, cnt = int(robot_num), int(cnt)
    
    i, j, k = robot[robot_num]

    if command == 'F':
        while cnt > 0:
            ni, nj = i+di[k], j+dj[k]
            
            if ni < 0 or ni > B-1 or nj < 0 or nj > A-1:
                ret = f'Robot {robot_num} crashes into the wall'
                flag = True
                break

            if board[ni][nj] != 0:
                ret = f'Robot {robot_num} crashes into robot {board[ni][nj]}'
                flag = True
                break

            i, j = ni, nj
            cnt -= 1

        if flag:
            print(ret)
            break

        i, j, k = robot[robot_num]
        board[i][j] = 0
        board[ni][nj] = robot_num
        robot[robot_num] = [ni, nj, k]
        
    elif command == 'L':
        robot[robot_num][2] = k-(1*cnt)%4
    elif command == 'R':
        robot[robot_num][2] = (k+1*cnt)%4

else:
    print(ret)