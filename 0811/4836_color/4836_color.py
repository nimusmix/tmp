T = int(input())

for tc in range(1, T+1):
    board = [['0'] * 10 for _ in range(10)]
    N = int(input())
    purple = 0

    for i in range(N):
        r1, c1, r2, c2, C = map(int, input().split())

        if C == 1: C = 'R'
        else: C = 'B'

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                board[j][k] += C

    for j in range(10):
        for k in range(10):
            if 'R' in board[j][k] and 'B' in board[j][k]:
                purple += 1

    print(f'#{tc} {purple}')
