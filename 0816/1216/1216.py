import sys
# sys.stdin = open('input.txt')
sys.stdin = open('회문2_input.txt')

for _ in range(10):
    tc = '#' + input()

    board = [list(input()) for _ in range(100)]
    maxlen = 0

    for i in board:
        for j in range(100):
            for k in range(1, 101):
                check = i[j:j+k+1]
                if check == check[::-1] and len(check) > maxlen:
                    maxlen = len(check)

    new_board = zip(*board)
    for i in new_board:
        for j in range(100):
            for k in range(1, 101):
                check = i[j:j+k+1]
                if check == check[::-1] and len(check) > maxlen:
                    maxlen = len(check)

    print(f'{tc} {maxlen}')