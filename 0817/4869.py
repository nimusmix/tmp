T = int(input())

for tc in range(1, T+1):
    width = int(input())

    data = divmod(width//10, 2)

    cnt = 1
    N = data[0]

    while N != 0:
        if data[1] == 0:
            cnt = cnt * 4 - 1
            N -= 1
        else:
            cnt = cnt * 4 + 1
            N -= 1

    print(f'#{tc} {cnt}')