T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = []
    cnt = 0
    idx = N

    for i in range(N):
        queue.append((i+1, cheese[i]))

    while cnt < M-1:
        i, pizza = queue.pop(0)

        if pizza == 0:
            if idx < M:
                queue.append((idx+1, cheese[idx]//2))
            idx, cnt = idx+1, cnt+1
        else:
            queue.append((i, pizza // 2))

    print(f'#{tc} {queue[0][0]}')