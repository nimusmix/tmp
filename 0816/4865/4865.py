import copy

T = int(input())

for tc in range(1, T+1):
    N = list(set(input()))
    M = list(input())

    maxV = 0

    for al in N:
        cnt = 0
        MM = copy.deepcopy(M)
        while al in MM:
            cnt += 1
            MM.pop(MM.index(al))
        else:
            if cnt > maxV:
                maxV = cnt

    print(f'#{tc} {maxV}')