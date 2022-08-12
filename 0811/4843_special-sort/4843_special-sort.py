T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    o_li = [0] * N

    li.sort()

    r_li = sorted(li, reverse=1)

    j = 0
    for i in range(N):
        if i % 2 == 0:
            o_li[i] = r_li[j]
        else:
            o_li[i] = li[j]
            j += 1

    print(f'#{tc}', end=' ')
    print(*o_li[:10])