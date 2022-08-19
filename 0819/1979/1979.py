import sys
sys.stdin = open('input (4).txt')

def my_sum(li):
    result = 0
    for s in li:
        result += s
    return result

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    board = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    new_board = list(zip(*board))
    cnt = 0

    for k in board, new_board:
        for i in range(1, N+1):
            for j in range(1, N-K+2):
                if my_sum(k[i][j:j+K]) == K and k[i][j-1] == 0 and k[i][j+K] == 0:
                    cnt += 1

    print(f'#{tc} {cnt}')