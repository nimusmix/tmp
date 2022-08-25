import sys
sys.stdin = open('sample_input (3).txt')

T = int(input())

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(x, y):
    global find

    if maze[x][y] == '3':
        find = 1
        return
    else:
        maze[x][y] = '-1'
        for k in direction:
            if -1 < x+k[0] < N and -1 < y+k[1] < N:
                if maze[x+k[0]][y+k[1]] == '0' or maze[x+k[0]][y+k[1]] == '3':
                    dfs(x+k[0], y+k[1])

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    find = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                s_idx = (i, j)

    dfs(s_idx[0], s_idx[1])
    print(f'#{tc} {find}')