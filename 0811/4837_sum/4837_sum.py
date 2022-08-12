T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    a = list(range(1, 13))

    cnt = 0

    for i in range(1, 1<<12):
        sumLi = []
        sumV = 0
        for j in range(12):
            if i & (1<<j):
                sumLi.append(a[j])
        if len(sumLi) == N:
            for k in sumLi:
                sumV += k
            if sumV == K:
                cnt += 1

    print(f'#{tc} {cnt}')