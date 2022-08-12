import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    ei = 99
    for j in range(100):
        if board[99][j] == 2:
            ej = j

    while ei >= 0:
        if ej-1 >= 0 and board[ei][ej-1] == 1:
            ej -= 1
        elif ej+1 <= 99 and board[ei][ej+1] == 1:
            ej += 1
        else:
            ei -= 1

        board[ei][ej] = 2

    print(f'#{tc} {ej}')