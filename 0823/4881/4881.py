import sys
sys.stdin = open('sample_input (4).txt')

T = int(input())

def f(i, N):
    if i == N:
        for i in range(N):
            if bit[i]:
                print(A[i], end=' ')
        print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = list(range(5))
bit = [0] * 5
f(0, 5)

# for tc in range(1, T+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     sumV = 0
#     j_li = []
#
#     for i in range(N):
#         tmp = 99
#         for j in range(N):
#             if board[i][j] < tmp and j not in j_li:
#                 tmp = board[i][j]
#         j_li.append(board[i].index(tmp))
#
#         print(tmp)
#         sumV += tmp
#
#     print(f'#{tc} {sumV}')