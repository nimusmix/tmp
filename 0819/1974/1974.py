import sys
sys.stdin = open('input (6).txt')

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = 1

    for x in range(9):
        c_li = [0] * 10
        for y in range(9):
            c_li[sudoku[x][y]] = 1
        if 0 in c_li[1:]:
            flag = 0

    for y in range(9):
        c_li = [0] * 10
        for x in range(9):
            c_li[sudoku[x][y]] = 1
        if 0 in c_li[1:]:
            flag = 0

    for y in range(0,7,3):
        c_li = [0] * 10
        for x in range(0,7,3):
            square = []
            for k in range(3):
                square.extend(sudoku[y+k][x:x+3])
            for i in square:
                c_li[i] = 1
            if 0 in c_li[1:]:
                flag = 0

    print(f'#{tc} {flag}')