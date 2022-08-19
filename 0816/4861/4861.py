import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    for i in board:                                    # 가로
        for j in range(N-M+1):
            check = i[j:j+M+1]
            if check == check[::-1]:
                print(f'#{tc}', end=' ')
                print(''.join(check))

    # new_board = zip(*board)

    for i in range(N):
        for j in range(N):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in board:                                # 세로
        for j in range(N-M+1):
            check = i[j:j+M+1]
            if check == check[::-1]:
                print(f'#{tc}', end=' ')
                print(''.join(check))